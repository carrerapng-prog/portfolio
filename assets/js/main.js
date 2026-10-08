(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Navigation: beim Scrollen kompakt, per Klick aufklappbar
  const nav = document.querySelector("[data-nav]");
  if (nav) {
    const toggle = nav.querySelector(".nav-toggle");
    const onScroll = () => {
      const compact = scrollY > 120;
      nav.classList.toggle("is-compact", compact);
      if (!compact) nav.classList.remove("is-open");
    };
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open);
    });
  }

  // Elemente beim Scrollen einblenden
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("is-visible"); io.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  document.querySelectorAll(".reveal").forEach((el) => io.observe(el));

  // Videos nur abspielen, wenn sie sichtbar sind
  const vio = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      const v = e.target;
      if (e.isIntersecting && !reduce) v.play().catch(() => {});
      else v.pause();
    });
  }, { threshold: 0.35 });
  document.querySelectorAll("video[data-autoplay]").forEach((v) => {
    vio.observe(v);
    // Hochformat-Videos automatisch schmaler darstellen
    v.addEventListener("loadedmetadata", () => {
      if (v.videoHeight > v.videoWidth) v.parentElement.classList.add("media-vertical");
    });
  });

  // Kartenstapel im Hero
  const stack = document.querySelector("[data-stack]");
  if (stack) {
    const cards = [...stack.children];
    let order = cards.map((_, i) => i);
    const paint = () => order.forEach((c, pos) => (cards[c].dataset.pos = pos));
    paint();
    setTimeout(() => stack.classList.add("is-ready"), 150);
    if (!reduce && cards.length > 1) {
      setInterval(() => {
        if (document.hidden) return;
        const top = cards[order[0]];
        top.classList.add("is-leaving");
        setTimeout(() => {
          top.classList.remove("is-leaving");
          order.push(order.shift());
          paint();
        }, 550);
      }, 3200);
    }
  }

  // Wechselnde Wörter im Footer
  document.querySelectorAll(".words").forEach((box) => {
    const words = [...box.children];
    if (words.length < 2 || reduce) return;
    let i = 0;
    setInterval(() => {
      const cur = words[i];
      i = (i + 1) % words.length;
      const next = words[i];
      cur.classList.remove("is-active");
      cur.classList.add("is-out");
      next.classList.remove("is-out");
      next.classList.add("is-active");
      box.setAttribute("aria-label", next.textContent);
      setTimeout(() => cur.classList.remove("is-out"), 700);
    }, 2400);
  });
})();
