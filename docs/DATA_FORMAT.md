# Ejemplo de Estructura de Datos

## Archivo Excel Requerido

### Nombre del archivo
`Socios_YYYY.xlsx` (por ejemplo: `Socios_2026.xlsx`)

### Estructura

#### Fila 1: Encabezados (opcional, se ignora)
```
Lista de socios | | | | | |
```

#### Fila 2: Columnas (REQUERIDO)
```
Número | Nombre | Apellido Paterno | Apellido Materno | Rut | Dirección | Profesión
```

#### Filas 3+: Datos
```
1 | Juan | Pérez | González | 12345678-9 | Calle 123 | Ingeniero
2 | María | López | Soto | 98765432-1 | Av. Principal | Profesora
...
```

### Columnas Requeridas

Solo estas columnas son necesarias para el sistema:

1. **Nombre** (columna B)
2. **Apellido Paterno** (columna C)
3. **Apellido Materno** (columna D)
4. **Rut** (columna E)

Las demás columnas (Dirección, Profesión, etc.) se ignoran.

### Formato del RUT

Acepta cualquiera de estos formatos:
- `12345678-9` ✅ (recomendado)
- `12.345.678-9` ✅
- `12345678-K` ✅ (con K mayúscula)

**NO acepta:**
- `123456789` ❌ (sin guión)
- `12.345.678-k` ❌ (k minúscula, debe ser mayúscula)

### Ejemplo Completo

```
# FILA 1 (ignorada)
Lista de socios Actualizado 2026

# FILA 2 (headers)
| Nombre  | Apellido Paterno | Apellido Materno | Rut          | Dirección    | Profesión  |
|---------|------------------|------------------|--------------|--------------|------------|
| Juan    | Pérez            | González         | 12345678-9   | Calle 123    | Ingeniero  |
| María   | López            | Soto             | 98765432-1   | Av. Principal| Profesora  |
| Pedro   | Ramírez          | Torres           | 11222333-K   |              |            |
```

**Notas:**
- Las columnas Dirección y Profesión pueden estar vacías
- El sistema solo usa: Nombre, Apellido Paterno, Apellido Materno, y Rut

---

## CSV Alternativo (Futuro)

Si prefieres CSV en lugar de Excel, el formato sería:

```csv
Nombre,Apellido Paterno,Apellido Materno,Rut
Juan,Pérez,González,12345678-9
María,López,Soto,98765432-1
Pedro,Ramírez,Torres,11222333-K
```

**Nota:** Actualmente el script solo soporta Excel (.xlsx), pero es fácil adaptarlo para CSV.

---

## Validación

Antes de procesar, verifica:

- [ ] Archivo tiene extensión `.xlsx`
- [ ] Fila 2 tiene los headers correctos
- [ ] Columna RUT tiene formato correcto
- [ ] No hay RUTs duplicados
- [ ] Todos los nombres están completos

---

## Troubleshooting

### Error: "Rut column not found"

**Solución:** Verifica que la columna se llame exactamente "Rut" en la fila 2

### Error: "Invalid RUT format"

**Solución:** Revisa que los RUTs tengan guión: `12345678-9`

### Warning: "Empty name"

**Solución:** Completa los nombres faltantes en el Excel

---

**Tip:** Guarda siempre una copia de backup de tu Excel antes de generar el HTML.
