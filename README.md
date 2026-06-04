# Vínculo Técnico - Sitio Web Corporativo

Este repositorio contiene el código fuente del sitio web estático para **Vínculo Técnico**, una consultora de activos y gestión del mantenimiento ubicada en Colombia. 

## Arquitectura del Proyecto

El proyecto está construido bajo una arquitectura **Vanilla HTML, CSS y JS**, elegida específicamente por su:
- **Simplicidad:** Sin dependencias complejas (sin Node.js, Webpack, etc.).
- **Rendimiento:** Carga instantánea al ser archivos estáticos puros.
- **Compatibilidad:** 100% compatible para despliegue directo en **GitHub Pages**.
- **Principios SOLID:** La estructura CSS y JS ha sido modularizada para mantener una responsabilidad única por archivo (SRP).

## Estructura de Carpetas

```text
├── assets/
│   ├── css/
│   │   ├── components/  # Estilos de componentes específicos (ej. botones)
│   │   ├── layout/      # Estilos estructurales (header, footer)
│   │   ├── base.css     # Estilos base y tipografía
│   │   ├── reset.css    # Normalización entre navegadores
│   │   ├── styles.css   # Archivo principal que importa todos los demás
│   │   └── variables.css# Sistema de diseño (colores, fuentes, espaciados)
│   └── js/
│       ├── components/  # Lógica de componentes interactivos (ej. Header.js)
│       ├── core/        # Utilidades transversales (ej. Logger.js)
│       └── app.js       # Punto de entrada principal de JS
├── casos-exito.html     # Página de Casos de Éxito
├── contacto.html        # Página de Contacto
├── Gemini.md            # Guía Maestra de Identidad Visual y Arquitectura
├── index.html           # Página de Inicio (Home)
├── nosotros.html        # Página sobre la empresa
├── recursos.html        # Página de Recursos / Blog
└── servicios.html       # Página de Servicios
```

## Identidad Visual

Toda la interfaz visual (colores, tipografía y lineamientos de marca) está documentada exhaustivamente en el archivo `Gemini.md`. Los estilos en `variables.css` son una traducción directa de dicho documento de diseño.

## Desarrollo Local

Dado que el sitio no requiere un proceso de compilación (build step), puedes visualizarlo simplemente abriendo el archivo `index.html` en cualquier navegador web moderno. 

Para una mejor experiencia de desarrollo (especialmente para resolver rutas absolutas o probar módulos JS localmente), se recomienda utilizar una extensión como "Live Server" en VS Code o ejecutar un servidor HTTP simple de Python:

```bash
python -m http.server 8000
```
*(Y luego acceder a `http://localhost:8000` en tu navegador)*

## Despliegue

El sitio está diseñado para ser alojado en **GitHub Pages**. Cada commit subido a la rama principal (`main`) se reflejará en la web en vivo automáticamente si GitHub Pages está activado en la configuración del repositorio y apuntando a la rama raíz (root).
