# Scripts

## generar_html.py

Script Python para generar el archivo `index.html` con datos actualizados de socios.

### Requisitos

```bash
pip install -r ../requirements.txt
```

### Uso

```bash
python generar_html.py archivo_socios.xlsx [imagen_banner.jpg]
```

### Parámetros

- `archivo_socios.xlsx`: Archivo Excel con los datos de socios (requerido)
- `imagen_banner.jpg`: Imagen para el banner (opcional)

### Formato del Excel

El archivo Excel debe tener estas columnas (en la fila 2):

| Nombre | Apellido Paterno | Apellido Materno | Rut |
|--------|------------------|------------------|-----|
| Juan   | Pérez            | González         | 12345678-9 |
| María  | López            | Soto             | 98765432-1 |

**Notas:**
- La primera fila puede tener títulos (se ignora)
- El RUT debe incluir guión: `12345678-9`
- Puede tener puntos o no: `12.345.678-9` o `12345678-9`

### Ejemplo

```bash
# Con imagen de banner
python generar_html.py socios_2026.xlsx banner.jpg

# Sin imagen de banner
python generar_html.py socios_2026.xlsx
```

### Output

El script genera:
- `index.html`: Archivo listo para subir a Netlify

### Datos de Seguridad

El script:
- ✅ Hashea los RUTs con SHA-256
- ✅ No guarda los RUTs originales en el HTML
- ✅ Solo incluye nombres y hashes
- ⚠️ Los nombres SÍ son visibles en el código fuente

---

## Notas de Desarrollo

Para mejorar este script:

1. **Validación más robusta**
   - Validar RUTs antes de procesar
   - Detectar duplicados
   - Alertar sobre formatos inválidos

2. **Logging**
   - Guardar log de procesamiento
   - Registro de errores

3. **Testing**
   - Unit tests para validación de RUT
   - Tests de integración

4. **CLI mejorado**
   - Argumentos con `argparse`
   - Flags para opciones adicionales

