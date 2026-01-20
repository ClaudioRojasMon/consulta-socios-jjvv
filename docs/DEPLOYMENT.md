# 🚀 Guía de Deployment

Esta guía cubre diferentes opciones para publicar tu sistema de consulta de socios.

## 📋 Pre-requisitos

- Archivo `index.html` generado
- Cuenta en la plataforma de hosting elegida (todas son gratuitas)

---

## Opción 1: Netlify (Recomendado) ⭐

### A. Deploy desde GitHub

1. **Sube tu código a GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/TU-USUARIO/TU-REPO.git
   git push -u origin main
   ```

2. **Conecta con Netlify**
   - Ve a [Netlify](https://app.netlify.com)
   - Clic en "New site from Git"
   - Selecciona tu repositorio
   - Deploy automático

3. **Configuración**
   - Build command: (dejar vacío)
   - Publish directory: `/`
   - Deploy

### B. Deploy Manual (Drag & Drop)

1. **Ve a Netlify**
   - [app.netlify.com](https://app.netlify.com)
   - Inicia sesión o crea cuenta

2. **Crea carpeta**
   ```
   mi-proyecto/
   └── index.html
   ```

3. **Arrastra carpeta**
   - Arrastra carpeta completa a Netlify
   - Espera 30 segundos
   - ¡Listo!

4. **Personalizar dominio**
   - Site settings → Domain management
   - Change site name
   - Ejemplo: `consulta-socios-jjvv.netlify.app`

### Ventajas de Netlify
- ✅ Gratis permanentemente
- ✅ HTTPS automático
- ✅ Deploy en segundos
- ✅ Actualizaciones simples (drag & drop)
- ✅ URL personalizable

---

## Opción 2: Vercel

### Deploy

1. **Instala Vercel CLI (opcional)**
   ```bash
   npm i -g vercel
   vercel
   ```

2. **O usa la interfaz web**
   - Ve a [vercel.com](https://vercel.com)
   - Import Project
   - Arrastra tu carpeta

### URL Final
`https://tu-proyecto.vercel.app`

---

## Opción 3: GitHub Pages

### Setup

1. **Sube a GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push
   ```

2. **Activa GitHub Pages**
   - Repositorio → Settings → Pages
   - Source: main branch
   - Folder: / (root)
   - Save

3. **Espera 1-2 minutos**

### URL Final
`https://TU-USUARIO.github.io/TU-REPO`

---

## Opción 4: Hosting Tradicional

### Si tienes cPanel u otro hosting:

1. **Descarga index.html**

2. **Sube vía FTP o File Manager**
   - Carpeta: `/public_html/consulta-socios/`

3. **Accede**
   - `https://tudominio.com/consulta-socios/`

---

## 🔄 Actualizar el Sitio

### Netlify

**Método 1: Drag & Drop**
1. Ve a tu sitio en Netlify
2. Deploys tab
3. Arrastra nuevo `index.html`

**Método 2: Git Push**
```bash
git add index.html
git commit -m "Update: agregar nuevos socios"
git push
```
Netlify detecta el push y redeploya automáticamente

### Vercel

Similar a Netlify:
```bash
vercel --prod
```

### GitHub Pages

```bash
git add index.html
git commit -m "Update data"
git push
```
GitHub Pages se actualiza automáticamente

---

## 📊 Configuración Recomendada

### Variables de Entorno (si usas backend futuro)

Netlify/Vercel:
```bash
# No aplica actualmente (todo es client-side)
# Pero si agregas backend:
DATABASE_URL=...
API_KEY=...
```

### Headers de Seguridad

Crear archivo `netlify.toml`:

```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

---

## ✅ Checklist Post-Deployment

- [ ] Sitio accesible desde URL pública
- [ ] Probar en móvil
- [ ] Probar en desktop
- [ ] Validar con RUTs de prueba
- [ ] Verificar imagen de banner
- [ ] Confirmar textos correctos
- [ ] Compartir URL por WhatsApp/Email

---

## 🔧 Troubleshooting

### Problema: La imagen no se ve

**Solución:**
- Verifica que la imagen esté en Base64 en el HTML
- O sube imagen por separado y actualiza la URL en CSS

### Problema: El sitio no actualiza

**Solución:**
- Limpia caché del navegador (Ctrl + Shift + R)
- En Netlify: Trigger deploy manual
- Verifica que subiste el archivo correcto

### Problema: Error 404

**Solución:**
- Verifica que el archivo se llama `index.html`
- Revisa que esté en la raíz del proyecto

---

## 📱 Dominio Personalizado (Opcional)

### Comprar dominio

1. **Compra en:**
   - Namecheap
   - Google Domains
   - GoDaddy

2. **Configura DNS:**
   - En Netlify: Site settings → Domain management → Add custom domain
   - Sigue instrucciones de DNS

3. **Ejemplo:**
   - De: `consulta-socios-jjvv.netlify.app`
   - A: `socios.jjvvmiradorquilen.cl`

---

## 💰 Costos

- **Netlify**: $0/mes (Free tier suficiente)
- **Vercel**: $0/mes (Free tier suficiente)
- **GitHub Pages**: $0/mes (Gratis)
- **Dominio personalizado**: ~$10-15/año (opcional)

---

**¿Preguntas?** Abre un issue en GitHub o contacta al mantenedor.
