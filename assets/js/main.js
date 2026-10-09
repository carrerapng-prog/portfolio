(() => {
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Navigation: beim Scrollen kompakt, per Klick aufklappbar
  const nav = document.querySelector("[data-nav]");
  if (nav) {
    const toggle = nav.querySelector(".nav-toggle");
    const onScroll = () => {
      const compact = scrollY > 120;
      nav.classList.toggle("is-compact", compact);
      if (!compact) { nav.classList.remove("is-open"); toggle.setAttribute("aria-expanded", false); }
    };
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    const setOpen = (open) => {
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open);
      toggle.setAttribute("aria-label", open ? "Menü schließen" : "Menü öffnen");
    };
    toggle.addEventListener("click", () => setOpen(!nav.classList.contains("is-open")));
    // Escape schließt das Menü
    addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nav.classList.contains("is-open")) { setOpen(false); toggle.focus(); }
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

  // Kartenstapel im Hero: läuft automatisch, Karten und Punkte sind anklickbar
  const stack = document.querySelector("[data-stack]");
  if (stack) {
    const cards = [...stack.children];
    const dots = [...document.querySelectorAll("[data-stack-dots] .stack-dot")];
    const pauseBtn = document.querySelector(".stack-pause");
    let order = cards.map((_, i) => i);
    let busy = false;
    const paint = () => {
      order.forEach((c, pos) => {
        cards[c].dataset.pos = pos;
        // Nur die vordere Karte ist per Tastatur erreichbar; hintere über die Punkte
        cards[c].tabIndex = pos === 0 ? 0 : -1;
        cards[c].setAttribute("aria-hidden", pos === 0 ? "false" : "true");
      });
      dots.forEach((d, i) => {
        d.classList.toggle("is-active", i === order[0]);
        d.setAttribute("aria-current", i === order[0] ? "true" : "false");
      });
    };
    // Karte i nach vorne holen
    const show = (i) => {
      if (busy || order[0] === i) return;
      busy = true;
      const top = cards[order[0]];
      top.classList.add("is-leaving");
      setTimeout(() => {
        top.classList.remove("is-leaving");
        while (order[0] !== i) order.push(order.shift());
        paint();
        busy = false;
      }, 450);
    };
    const next = () => show(order[1]);
    paint();
    setTimeout(() => stack.classList.add("is-ready"), 150);

    cards.forEach((card, i) => card.addEventListener("click", (e) => {
      if (order[0] !== i) { e.preventDefault(); show(i); restart(); }
    }));
    dots.forEach((dot, i) => dot.addEventListener("click", () => { show(i); restart(); }));

    let timer = null, hovering = false, focused = false, paused = reduce;
    const restart = () => {
      clearInterval(timer);
      if (paused || cards.length < 2) return;
      timer = setInterval(() => { if (!document.hidden && !hovering && !focused) next(); }, 3000);
    };
    const wrap = stack.parentElement;
    wrap.addEventListener("mouseenter", () => (hovering = true));
    wrap.addEventListener("mouseleave", () => (hovering = false));
    wrap.addEventListener("focusin", () => (focused = true));
    wrap.addEventListener("focusout", () => (focused = false));
    if (pauseBtn) {
      const syncPause = () => {
        pauseBtn.setAttribute("aria-pressed", paused);
        pauseBtn.setAttribute("aria-label", paused ? "Automatischen Wechsel starten" : "Automatischen Wechsel pausieren");
      };
      pauseBtn.addEventListener("click", () => { paused = !paused; syncPause(); restart(); });
      syncPause();
    }
    restart();
  }

  // Wechselnde Wörter im Footer: im Text steht immer nur das aktuelle Wort
  document.querySelectorAll("[data-words]").forEach((box) => {
    const words = box.dataset.words.split(",");
    if (words.length < 2 || reduce) return;
    let i = 0;
    setInterval(() => {
      if (document.hidden) return;
      i = (i + 1) % words.length;
      const cur = box.querySelector(".word.is-active");
      const next = document.createElement("span");
      next.className = "word";
      next.textContent = words[i];
      box.appendChild(next);
      void next.offsetWidth; // Startzustand rendern, damit die Einblendung animiert
      next.classList.add("is-active");
      cur.classList.remove("is-active");
      cur.classList.add("is-out");
      cur.setAttribute("aria-hidden", "true");
      setTimeout(() => cur.remove(), 700);
    }, 2400);
  });
})();
