# 👥 Sistema de Consulta de Socios - JJVV Mirador Quilen

[![Netlify Status](https://img.shields.io/badge/netlify-deployed-success)](https://consulta-socios-mirador-quilen.netlify.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Sistema web para consulta privada de socios de la Junta de Vecinos Mirador Quilen, Puerto Varas, Chile.

🔗 **Demo en vivo:** [https://consulta-socios-mirador-quilen.netlify.app](https://consulta-socios-mirador-quilen.netlify.app)

![Banner](docs/screenshot.png)

## 📋 Características

✅ **Privacidad total** - Los RUTs están encriptados usando SHA-256  
✅ **Validación automática** - Valida RUTs chilenos antes de buscar  
✅ **Diseño responsive** - Funciona perfectamente en móviles y computadores  
✅ **Banner personalizado** - Muestra foto panorámica de Mirador Quilen  
✅ **Cero dependencias externas** - Todo contenido en un solo archivo HTML  
✅ **Deployment simple** - Listo para Netlify, Vercel, o GitHub Pages  

## 🎯 Propósito

Este sistema permite a los vecinos verificar su membresía sin exponer la lista completa de socios, protegiendo la privacidad de todos los miembros.

## 🚀 Cómo funciona

1. El usuario ingresa su RUT (con o sin formato)
2. El sistema valida que sea un RUT chileno válido
3. Normaliza el RUT al formato estándar
4. Genera un hash SHA-256 del RUT
5. Busca el hash en la base de datos encriptada
6. Muestra si es socio y su nombre (sin exponer otros datos)

## 🛠️ Tecnologías

- **HTML5** - Estructura
- **CSS3** - Diseño y animaciones
- **JavaScript ES6+** - Lógica de validación y búsqueda
- **Web Crypto API** - Encriptación SHA-256
- **Base64** - Codificación de imagen

## 📦 Instalación

### Opción 1: Clonar y usar localmente

```bash
git clone https://github.com/TU-USUARIO/consulta-socios-jjvv.git
cd consulta-socios-jjvv
# Abrir index.html en tu navegador
```

### Opción 2: Deploy en Netlify

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy)

1. Haz fork de este repositorio
2. Conecta tu repositorio a Netlify
3. Deploy automático

### Opción 3: Deploy manual

1. Descarga `index.html`
2. Súbelo a cualquier hosting estático
3. ¡Listo!

## 🔄 Actualizar base de datos de socios

### Requisitos
- Archivo Excel con columnas: `Nombre`, `Apellido Paterno`, `Apellido Materno`, `Rut`
- Python 3.x con pandas instalado

### Proceso

1. **Prepara tu Excel actualizado**
   ```
   Columnas requeridas:
   - Nombre
   - Apellido Paterno  
   - Apellido Materno
   - Rut (formato: 12345678-9)
   ```

2. **Genera el nuevo archivo HTML**
   ```bash
   python scripts/generar_html.py tu-archivo.xlsx
   ```

3. **Actualiza en Netlify**
   - Ve a Netlify → Deploys
   - Arrastra la carpeta con el nuevo `index.html`
   - Espera 30 segundos

4. **Verifica**
   - Abre tu sitio
   - Prueba con algunos RUTs
   - ¡Listo!

## 🔒 Seguridad y Privacidad

### ✅ Buenas prácticas implementadas:

- **Encriptación unidireccional (SHA-256)**: Los RUTs se hashean, no se pueden revertir
- **Sin almacenamiento**: No se guarda ningún dato del usuario
- **Sin tracking**: No hay analytics ni cookies
- **Sin servidor backend**: Todo funciona en el navegador del usuario
- **Código abierto**: Cualquiera puede verificar la seguridad

### ⚠️ Limitaciones conocidas:

- Los nombres de los socios están visibles en el código fuente
- Para máxima privacidad, considera implementar un backend con API

## 📱 Compartir por WhatsApp

Mensaje sugerido:

```
👥 Verificación de Socios 2026
JJVV Mirador Quilen

Verifica si estás registrado como socio:
🔗 https://consulta-socios-mirador-quilen.netlify.app

✓ Ingresa tu RUT
✓ Sistema confidencial
✓ 287 socios registrados

¿Dudas? Contáctame
```

## 🎨 Personalización

### Cambiar colores

Edita las variables CSS en el `<style>`:

```css
/* Gradiente principal */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Colores de éxito/error */
.result.success { background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); }
.result.error { background: linear-gradient(135deg, #fc8181 0%, #f56565 100%); }
```

### Cambiar imagen de banner

1. Convierte tu imagen a Base64 usando: https://base64.guru/converter/encode/image
2. Reemplaza el `data:image/jpeg;base64,...` en el CSS `.banner`

### Cambiar textos

Busca y reemplaza en el HTML:
- "JJVV Mirador Quilen" → Tu organización
- "Puerto Varas, Región de Los Lagos" → Tu ubicación
- "Consulta de Socios 2026" → Tu título

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👏 Créditos

### Desarrollado por:
- **Claudio Rojas** - Presidente JJVV Mirador Quilen
- Email: crojasmon@gmail.com

### Con la colaboración de:
- **Claude (Anthropic)** - Asistente de IA para desarrollo y diseño
  - Generación de código HTML/CSS/JavaScript
  - Implementación de seguridad (SHA-256)
  - Diseño responsive y UX
  - Optimización de performance

### Tecnologías:
- [Netlify](https://netlify.com) - Hosting
- [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) - Encriptación
- [Lucide Icons](https://lucide.dev/) - Iconografía (vía SVG)

## 📞 Contacto

**Junta de Vecinos Mirador Quilen**  
Puerto Varas, Región de Los Lagos, Chile

Para consultas sobre membresía o el sistema, contacta a la directiva de la JJVV.

---

## 🌟 Screenshots

### Vista Desktop
![Desktop View](docs/desktop-view.png)

### Vista Mobile
![Mobile View](docs/mobile-view.png)

### Resultado Exitoso
![Success State](docs/success-state.png)

---

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub**

---

*Última actualización: Enero 2026*
