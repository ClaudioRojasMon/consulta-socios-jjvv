# 📚 Documentación Técnica

## Arquitectura del Sistema

### Resumen

Este es un sistema de consulta de socios completamente **client-side** (del lado del cliente), sin necesidad de servidor backend. Todo el procesamiento ocurre en el navegador del usuario.

## 🏗️ Componentes

### 1. Base de Datos Encriptada

```javascript
const sociosData = {
  "hash_SHA256_del_RUT": {
    "nombre": "Nombre Completo",
    "es_socio": true
  },
  // ... más socios
}
```

**Características:**
- Los RUTs se hashean con SHA-256 (irreversible)
- Solo se almacenan: hash, nombre y estado de socio
- No se guarda información sensible adicional

### 2. Validación de RUT

Algoritmo estándar chileno:

```javascript
function validarRut(rut) {
  // 1. Limpiar formato
  rut = rut.replace(/\./g, '').replace(/-/g, '').trim().toUpperCase();
  
  // 2. Separar cuerpo y dígito verificador
  const cuerpo = rut.slice(0, -1);
  const dv = rut.slice(-1);
  
  // 3. Calcular dígito verificador esperado
  let suma = 0;
  let multiplicador = 2;
  
  for (let i = cuerpo.length - 1; i >= 0; i--) {
    suma += parseInt(cuerpo[i]) * multiplicador;
    multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
  }
  
  const dvEsperado = 11 - (suma % 11);
  const dvCalculado = dvEsperado === 11 ? '0' : 
                      dvEsperado === 10 ? 'K' : 
                      dvEsperado.toString();
  
  // 4. Comparar
  return dv === dvCalculado;
}
```

### 3. Normalización de RUT

Convierte cualquier formato a formato estándar:

```javascript
function normalizarRut(rut) {
  // Input: "12.345.678-9" o "123456789" o "12345678-9"
  // Output: "12345678-9"
  
  rut = rut.replace(/\./g, '').replace(/-/g, '').trim().toUpperCase();
  const cuerpo = rut.slice(0, -1);
  const dv = rut.slice(-1);
  return `${cuerpo}-${dv}`;
}
```

### 4. Encriptación SHA-256

Usa la Web Crypto API nativa del navegador:

```javascript
async function hashRut(rut) {
  const encoder = new TextEncoder();
  const data = encoder.encode(rut);
  const hashBuffer = await crypto.subtle.digest('SHA-256', data);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}
```

**Ejemplo:**
```
RUT: 12345678-9
Hash: a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3
```

## 🔐 Seguridad

### ¿Qué está protegido?

✅ **RUTs hasheados**
- Imposible revertir el hash a RUT original
- Cada RUT genera un hash único
- Algoritmo criptográfico estándar (SHA-256)

✅ **Sin almacenamiento**
- No se guardan cookies
- No se almacena localStorage
- No hay tracking

✅ **Sin servidor**
- Todo funciona en el navegador
- No hay base de datos externa
- No hay API calls

### ¿Qué NO está protegido?

⚠️ **Nombres visibles**
- Los nombres están en el código fuente
- Cualquiera puede ver el código HTML
- Si esto es un problema, considera backend

⚠️ **Búsqueda por fuerza bruta**
- Alguien podría probar todos los RUTs chilenos
- Para alta seguridad, implementa rate limiting en backend

## 📊 Flujo de Datos

```
Usuario ingresa RUT
    ↓
Validación (¿es RUT válido?)
    ↓
Normalización (formato estándar)
    ↓
Hash SHA-256
    ↓
Búsqueda en diccionario
    ↓
Mostrar resultado
```

## 🎨 Diseño Responsive

### Breakpoints

```css
/* Desktop: default */
.container { padding: 48px; }

/* Mobile: < 640px */
@media (max-width: 640px) {
  .content { padding: 32px 24px; }
  .banner { height: 150px; }
}
```

### Componentes Adaptables

- **Banner**: 200px desktop, 150px mobile
- **Padding**: 48px desktop, 24px mobile
- **Font sizes**: Escalados proporcionalmente

## 🚀 Performance

### Optimizaciones

1. **Imagen en Base64**
   - Pro: Cero HTTP requests adicionales
   - Con: Aumenta tamaño HTML (~30-50KB)
   - Alternativa: CDN externo

2. **CSS Inline**
   - Pro: Render inmediato
   - Con: No cacheable
   - Decisión: OK para archivo único

3. **JavaScript Inline**
   - Pro: Sin dependencias externas
   - Con: Cada carga descarga todo
   - Decisión: OK para ~5KB de JS

### Métricas Esperadas

- **First Contentful Paint**: < 1s
- **Time to Interactive**: < 2s
- **Total Bundle Size**: ~50KB (con imagen)

## 🧪 Testing

### Tests Manuales

Probar estos casos:

```
✅ RUT válido que es socio
✅ RUT válido que NO es socio
✅ RUT inválido
✅ Formatos: con puntos, sin puntos, con/sin guión
✅ Responsive: mobile, tablet, desktop
✅ RUT con K (dígito verificador K)
```

### Tests Automatizados (opcional)

```javascript
// Ejemplo con Jest
describe('validarRut', () => {
  test('valida RUT correcto', () => {
    expect(validarRut('12345678-9')).toBe(true);
  });
  
  test('rechaza RUT incorrecto', () => {
    expect(validarRut('12345678-0')).toBe(false);
  });
});
```

## 🔧 Mantenimiento

### Actualizar Base de Datos

1. **Preparar Excel**
   - Columnas: Nombre, Apellido Paterno, Apellido Materno, Rut

2. **Ejecutar script**
   ```bash
   python scripts/generar_html.py nuevo_archivo.xlsx imagen.jpg
   ```

3. **Deploy**
   - Subir `index.html` a Netlify
   - Verificar funcionamiento

### Cambiar Diseño

**Colores:**
```css
/* Buscar y reemplazar */
#667eea → tu-color-primario
#764ba2 → tu-color-secundario
```

**Textos:**
```html
<!-- Buscar y reemplazar -->
"JJVV Mirador Quilen" → "Tu organización"
"Puerto Varas..." → "Tu ubicación"
```

## 📱 Progressive Web App (Futuro)

Para convertir en PWA:

1. Agregar `manifest.json`
2. Implementar Service Worker
3. Hacer funcional offline
4. Agregar a pantalla de inicio

## 🌐 Internacionalización (Futuro)

Para soportar múltiples idiomas:

1. Separar textos a archivo JSON
2. Implementar selector de idioma
3. Cargar textos dinámicamente

---

**Mantenido por:** Claudio Rojas  
**Última actualización:** Enero 2026
