# 🌐 Sitio Web Oficial – CTP Francisco J. Orlich

## 📌 Descripción general

Este repositorio contiene el desarrollo del **sitio web institucional del Colegio Técnico Profesional Francisco J. Orlich (Sarchí, Costa Rica)**.

El proyecto fue construido con **Flask (Python)** y está organizado por versiones, iniciando con una **Base Pública estable (Versión 1.0)** pensada para crecer de forma ordenada, segura y escalable.

El sitio está orientado a:

* Estudiantes
* Familias
* Personal docente y administrativo

⚠️ **Este proyecto no es un demo genérico**: corresponde a un colegio real.

---

## 🎯 Objetivo del proyecto

Crear una plataforma web institucional que:

* Centralice información oficial del colegio
* Sea clara, accesible y responsive
* Permita en el futuro la **administración de contenidos sin programar**
* Pueda escalar a nivel técnico y visual sin rehacer la base

---

## 🧩 Tecnologías utilizadas (Versión 1.0)

* **Python 3**
* **Flask** (renderizado de vistas)
* **HTML5**
* **CSS3** (estructura base)
* **JavaScript básico** (carga modular de menú y footer)

> No se utiliza base de datos ni autenticación real en esta versión.

---

## 🗂️ Estructura del proyecto

```
ctp_orlich_web/
│
├── app.py
├── static/
│   ├── style.css
│   ├── menu.html
│   └── footer.html
│
├── templates/
│   ├── index.html
│   ├── sobreNosotros.html
│   ├── anuncios.html
│   ├── concursos.html
│   ├── nuevosIngresos.html
│   └── login.html
│
└── README.md
```

---

## ✅ Versión 1.0 — Base Pública (COMPLETADA)

**Objetivo:** crear la estructura inicial, páginas principales y navegación.

### ✔ Checklist completado

* ✔ Estructura del proyecto
* ✔ Flask funcionando (app.py)
* ✔ Carpetas `templates/` y `static/`
* ✔ Página Inicio
* ✔ Página Sobre Nosotros (estructura base)
* ✔ Página Anuncios (estructura base)
* ✔ Página Concursos (estructura base)
* ✔ Página Nuevos Ingresos con submenú interno
* ✔ Menú global modular en todas las páginas
* ✔ Footer institucional modular
* ✔ Logo clickeable hacia login
* ✔ Formulario de login (solo visual)
* ✔ Responsive básico (estructura)
* ✔ Botón "volver arriba" en páginas largas

📌 **Estado:** Versión congelada y estable.

---

## 🔐 Login (estado actual)

* Login **solo visual**
* No hay autenticación real
* No hay roles separados

> En versiones futuras se utilizará **un único usuario y contraseña compartidos** para administración y docentes, según la dinámica real del colegio.

---

## 📜 Licencia

Este proyecto utiliza una **licencia personalizada**.

* ✔ Permitido: uso educativo y didáctico
* ❌ Prohibido: redistribución, comercialización o reutilización sin autorización

Ver el archivo `LICENSE` para más detalles.

---

## 🚀 Roadmap de versiones

### 🔵 Versión 2.0 — Administración

* Login funcional (usuario único)
* Panel administrativo
* CRUD de anuncios, concursos, ausencias, admitidos y becas
* Mensajes personalizados (errores, carga, sin conexión)

### 🟣 Versión 3.0 — Diseño profesional

* UI/UX institucional
* Responsive avanzado
* Iconografía, banners, mejoras visuales

### 🔴 Versión 4.0 — Seguridad

* Hash de contraseñas
* Protección CSRF / XSS / SQLi
* Validaciones de formularios

### 🟢 Versión 5.0 — Optimización

* Mejor rendimiento
* Organización avanzada de recursos

### 🟤 Versión 6.0 — Estética final

* Animaciones
* Interacciones suaves
* Versión final lista para presentación

---

## ✍️ Autora

Proyecto desarrollado por **Ana Belén Ulate Céspedes**.
Alias **XZER0**.

---

## 📎 Notas finales

Este repositorio representa una **base real, funcional y profesional**, pensada para crecer sin perder orden ni claridad.
