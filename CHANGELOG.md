# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-20

### Añadido
- Sistema de consulta de socios con validación de RUT
- Encriptación SHA-256 para protección de privacidad
- Banner personalizado con foto panorámica de Mirador Quilen
- Diseño responsive para móviles y escritorio
- Validación en tiempo real de RUT chileno
- Soporte para múltiples formatos de RUT (con/sin puntos y guión)
- Animaciones y transiciones suaves
- 287 socios iniciales en la base de datos
- Script Python para regenerar HTML con datos actualizados
- Documentación completa del proyecto
- Licencia MIT

### Características de Seguridad
- RUTs hasheados con SHA-256 (irreversible)
- Sin almacenamiento de datos del usuario
- Sin cookies ni tracking
- Arquitectura client-side (sin backend)

### Deployment
- Configurado para Netlify
- URL: https://consulta-socios-mirador-quilen.netlify.app

---

## [Unreleased]

### Por Hacer
- [ ] Agregar PWA (Progressive Web App) capabilities
- [ ] Implementar caché offline
- [ ] Agregar analytics (opcional)
- [ ] Tests automatizados
- [ ] CI/CD con GitHub Actions

---

**Formato de versiones:**
- MAJOR.MINOR.PATCH
- MAJOR: Cambios incompatibles con versiones anteriores
- MINOR: Nuevas funcionalidades compatibles
- PATCH: Correcciones de bugs
