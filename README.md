# Portfolio Ernesto Carrera

Sitio estático (HTML + CSS + JS), sin Framer ni dependencias.

## Editar contenido
1. Cambia textos, proyectos o medios en `content.py`.
2. Pon imágenes nuevas en `assets/img/` y videos en `assets/video/`.
3. Regenera las páginas:

       python3 build.py

## Ver en local

    python3 -m http.server 4321

y abre http://localhost:4321

## Estructura
- `index.html` – inicio
- `projects/` – lista de proyectos y una carpeta por proyecto
- `datenschutz/` – política de privacidad
- `assets/css/style.css`, `assets/js/main.js` – diseño y animaciones
- `assets/fonts/` – fuente Switzer (auto‑alojada)
