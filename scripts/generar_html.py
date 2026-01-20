#!/usr/bin/env python3
"""
Script para generar index.html con base de datos actualizada de socios
Uso: python generar_html.py archivo_socios.xlsx [ruta_imagen_banner.jpg]
"""

import sys
import json
import hashlib
import base64
import pandas as pd
from pathlib import Path

def hashear_rut(rut):
    """Genera hash SHA-256 de un RUT"""
    return hashlib.sha256(rut.encode()).hexdigest()

def procesar_excel(archivo_excel):
    """Lee archivo Excel y retorna diccionario de socios hasheados"""
    print(f"📖 Leyendo {archivo_excel}...")
    
    # Leer Excel
    df = pd.read_excel(archivo_excel, header=1)
    
    # Limpiar datos
    df = df.dropna(subset=['Rut'])
    df['Rut'] = df['Rut'].astype(str).str.strip()
    
    # Crear diccionario hasheado
    socios_data = {}
    for _, row in df.iterrows():
        rut = str(row['Rut']).strip()
        if rut and rut != 'nan':
            hash_rut = hashear_rut(rut)
            nombre_completo = f"{row.get('Nombre ', '')} {row.get('Apellido Paterno', '')}".strip()
            socios_data[hash_rut] = {
                'nombre': nombre_completo,
                'es_socio': True
            }
    
    print(f"✅ Procesados {len(socios_data)} socios")
    return socios_data

def imagen_a_base64(ruta_imagen):
    """Convierte imagen a base64"""
    if not ruta_imagen or not Path(ruta_imagen).exists():
        print("⚠️  No se encontró imagen de banner, usando placeholder")
        return ""
    
    with open(ruta_imagen, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def generar_html(socios_data, imagen_base64):
    """Genera el archivo HTML completo"""
    
    html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consulta de Socios - JJVV Mirador Quilen</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 24px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            animation: fadeIn 0.6s ease-out;
            overflow: hidden;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .banner {
            width: 100%;
            height: 200px;
            background-image: url(data:image/jpeg;base64,IMAGEN_BASE64);
            background-size: cover;
            background-position: center;
            position: relative;
        }
        .banner-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
            padding: 24px;
            color: white;
        }
        .banner-title {
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 4px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }
        .banner-subtitle {
            font-size: 16px;
            font-weight: 500;
            opacity: 0.95;
            text-shadow: 0 1px 2px rgba(0,0,0,0.3);
        }
        .content { padding: 48px; }
        .section-title {
            font-size: 20px;
            font-weight: 600;
            color: #1a202c;
            text-align: center;
            margin-bottom: 12px;
        }
        .subtitle {
            font-size: 15px;
            color: #718096;
            text-align: center;
            margin-bottom: 32px;
            line-height: 1.5;
        }
        label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            color: #4a5568;
            margin-bottom: 8px;
        }
        .input-group {
            position: relative;
            margin-bottom: 24px;
        }
        input {
            width: 100%;
            padding: 16px 16px 16px 48px;
            font-size: 18px;
            border: 2px solid #e2e8f0;
            border-radius: 12px;
            transition: all 0.3s ease;
        }
        input:focus {
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
        }
        .search-icon {
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            width: 20px;
            height: 20px;
            color: #a0aec0;
        }
        button {
            width: 100%;
            padding: 16px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        button:active { transform: translateY(0); }
        button:disabled {
            background: #cbd5e0;
            cursor: not-allowed;
            transform: none;
        }
        .error {
            color: #f56565;
            font-size: 14px;
            margin-top: 8px;
        }
        .result {
            margin-top: 32px;
            padding: 24px;
            border-radius: 16px;
            color: white;
            text-align: center;
            animation: slideIn 0.5s ease-out;
        }
        .result.success {
            background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        }
        .result.error {
            background: linear-gradient(135deg, #fc8181 0%, #f56565 100%);
        }
        .result-icon {
            width: 64px;
            height: 64px;
            background: rgba(255,255,255,0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 16px;
        }
        .result h2 {
            font-size: 24px;
            font-weight: 700;
            margin: 0 0 8px 0;
        }
        .result p {
            font-size: 18px;
            margin: 0;
            opacity: 0.9;
        }
        .footer {
            margin-top: 32px;
            padding-top: 24px;
            border-top: 1px solid #e2e8f0;
            text-align: center;
        }
        .footer p {
            font-size: 13px;
            color: #a0aec0;
        }
        .hint {
            font-size: 12px;
            color: #a0aec0;
            margin-top: 4px;
        }
        @media (max-width: 640px) {
            .content { padding: 32px 24px; }
            .banner { height: 150px; }
            .banner-title { font-size: 20px; }
            .banner-subtitle { font-size: 14px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="banner">
            <div class="banner-overlay">
                <div class="banner-title">JJVV Mirador Quilen</div>
                <div class="banner-subtitle">Puerto Varas, Región de Los Lagos</div>
            </div>
        </div>
        <div class="content">
            <h2 class="section-title">Consulta de Socios 2026</h2>
            <p class="subtitle">Ingresa tu RUT para verificar tu membresía</p>
            <div>
                <label for="rut">RUT</label>
                <div class="input-group">
                    <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                    </svg>
                    <input type="text" id="rut" placeholder="Ej: 12.433.959-6" onkeypress="if(event.key==='Enter') buscarSocio()">
                </div>
                <p class="hint">Puedes escribir con o sin puntos y guión</p>
                <div id="error" class="error" style="display:none;"></div>
            </div>
            <button onclick="buscarSocio()" id="btnBuscar">Consultar</button>
            <div id="resultado" style="display:none;"></div>
            <div class="footer">
                <p>Sistema confidencial • TOTAL_SOCIOS socios registrados • 2026</p>
            </div>
        </div>
    </div>
    <script>
        const sociosData = DATOS_SOCIOS;
        
        function validarRut(rut) {
            rut = rut.replace(/\./g, '').replace(/-/g, '').trim().toUpperCase();
            if (rut.length < 2) return false;
            const cuerpo = rut.slice(0, -1);
            const dv = rut.slice(-1);
            let suma = 0;
            let multiplicador = 2;
            for (let i = cuerpo.length - 1; i >= 0; i--) {
                suma += parseInt(cuerpo[i]) * multiplicador;
                multiplicador = multiplicador === 7 ? 2 : multiplicador + 1;
            }
            const dvEsperado = 11 - (suma % 11);
            const dvCalculado = dvEsperado === 11 ? '0' : dvEsperado === 10 ? 'K' : dvEsperado.toString();
            return dv === dvCalculado;
        }
        
        function normalizarRut(rut) {
            rut = rut.replace(/\./g, '').replace(/-/g, '').replace(/\s/g, '').trim().toUpperCase();
            if (rut.length < 2) return '';
            const cuerpo = rut.slice(0, -1);
            const dv = rut.slice(-1);
            return cuerpo + '-' + dv;
        }
        
        async function hashRut(rut) {
            const encoder = new TextEncoder();
            const data = encoder.encode(rut);
            const hashBuffer = await crypto.subtle.digest('SHA-256', data);
            const hashArray = Array.from(new Uint8Array(hashBuffer));
            return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
        }
        
        async function buscarSocio() {
            const input = document.getElementById('rut');
            const error = document.getElementById('error');
            const resultado = document.getElementById('resultado');
            const btnBuscar = document.getElementById('btnBuscar');
            const rut = input.value;
            
            error.style.display = 'none';
            resultado.style.display = 'none';
            
            if (!rut.trim()) {
                error.textContent = 'Por favor ingresa tu RUT';
                error.style.display = 'block';
                return;
            }
            
            const rutLimpio = rut.replace(/\./g, '').replace(/-/g, '').trim();
            
            if (!validarRut(rutLimpio)) {
                error.textContent = 'RUT inválido. Verifica que esté correcto';
                error.style.display = 'block';
                return;
            }
            
            btnBuscar.disabled = true;
            btnBuscar.textContent = 'Buscando...';
            
            try {
                const rutNormalizado = normalizarRut(rutLimpio);
                const hash = await hashRut(rutNormalizado);
                const socio = sociosData[hash];
                
                setTimeout(() => {
                    if (socio) {
                        resultado.className = 'result success';
                        resultado.innerHTML = `
                            <div class="result-icon">
                                <svg style="width:36px;height:36px;color:white;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                </svg>
                            </div>
                            <h2>¡Eres socio!</h2>
                            <p>${socio.nombre}</p>
                        `;
                    } else {
                        resultado.className = 'result error';
                        resultado.innerHTML = `
                            <div class="result-icon">
                                <svg style="width:36px;height:36px;color:white;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
                                </svg>
                            </div>
                            <h2>No encontrado</h2>
                            <p>Este RUT no está registrado como socio</p>
                        `;
                    }
                    resultado.style.display = 'block';
                    btnBuscar.disabled = false;
                    btnBuscar.textContent = 'Consultar';
                }, 800);
            } catch (err) {
                error.textContent = 'Ocurrió un error. Intenta nuevamente';
                error.style.display = 'block';
                btnBuscar.disabled = false;
                btnBuscar.textContent = 'Consultar';
            }
        }
    </script>
</body>
</html>"""
    
    # Reemplazar placeholders
    html = html_template.replace('IMAGEN_BASE64', imagen_base64)
    html = html.replace('DATOS_SOCIOS', json.dumps(socios_data, ensure_ascii=False))
    html = html.replace('TOTAL_SOCIOS', str(len(socios_data)))
    
    return html

def main():
    if len(sys.argv) < 2:
        print("❌ Uso: python generar_html.py archivo_socios.xlsx [ruta_imagen_banner.jpg]")
        sys.exit(1)
    
    archivo_excel = sys.argv[1]
    ruta_imagen = sys.argv[2] if len(sys.argv) > 2 else None
    
    print("\n🚀 Generando HTML para consulta de socios...\n")
    
    # Procesar datos
    socios_data = procesar_excel(archivo_excel)
    
    # Convertir imagen
    if ruta_imagen:
        print(f"🖼️  Procesando imagen: {ruta_imagen}")
        imagen_base64 = imagen_a_base64(ruta_imagen)
    else:
        imagen_base64 = ""
    
    # Generar HTML
    print("📝 Generando HTML...")
    html = generar_html(socios_data, imagen_base64)
    
    # Guardar archivo
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n✅ ¡Listo! Archivo generado: index.html")
    print(f"📊 Total de socios: {len(socios_data)}")
    print(f"\n📤 Próximo paso: Sube index.html a Netlify\n")

if __name__ == '__main__':
    main()
