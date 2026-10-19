"""
Script de alta fidelidad: Convierte foto real a SVG Matrix ASCII Art nítido
Estilo inspirado en gitskins.com / retro-futurista:
- Auto-crop centrado al rostro para máxima expresividad y definición.
- Matriz de caracteres tipográficos de ancho fijo con fuente Courier/monospace.
- Caracteres con espaciado constante y contraste ecualizado.
- Paleta Retro-Futurista: #05070B (fondo), #A855F7 (Purple), #E11D48 (Neon Red), #FF0055 (Crimson), #00FF66 (Terminal accent).
"""

import sys
import html
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

def generate_ascii_svg(image_path, output_svg_path, cols=62, rows=60):
    img = Image.open(image_path).convert('L') # Convert to grayscale
    
    # Auto-crop para enfocar rostro y cuello (evitar exceso de bordes vacíos)
    w, h = img.size
    # Centrado en el rostro
    crop_box = (int(w * 0.08), int(h * 0.04), int(w * 0.92), int(h * 0.90))
    img = img.crop(crop_box)
    
    # Ecualización y contraste optimizado
    img = ImageOps.autocontrast(img, cutoff=2)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.4)
    img = img.filter(ImageFilter.SHARPEN)
    
    # Resize to matrix grid
    img = img.resize((cols, rows), Image.Resampling.LANCZOS)
    
    # Ramp seleccionada para máxima legibilidad gitskins:
    # ramp = [" ", "·", ":", "-", "+", "*", "%", "#", "@", "█"]
    ramp = [" ", ".", ":", "-", "+", "=", "*", "%", "#", "@", "█"]
    num_levels = len(ramp)
    
    pixels = img.load()
    
    box_size = 500
    margin_x = 42
    margin_y = 48
    usable_w = box_size - (margin_x * 2)
    usable_h = box_size - (margin_y * 2) - 25
    
    step_y = usable_h / rows
    font_size = step_y * 1.05
    
    svg_lines = []
    svg_lines.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">')
    svg_lines.append('  <defs>')
    svg_lines.append('    <radialGradient id="spaceVignette" cx="50%" cy="50%" r="72%">')
    svg_lines.append('      <stop offset="0%" stop-color="#190B2A" />')
    svg_lines.append('      <stop offset="60%" stop-color="#090D16" />')
    svg_lines.append('      <stop offset="100%" stop-color="#05070B" />')
    svg_lines.append('    </radialGradient>')
    svg_lines.append('    <linearGradient id="cyberNeonGrad" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg_lines.append('      <stop offset="0%" stop-color="#E11D48" />')
    svg_lines.append('      <stop offset="45%" stop-color="#FF0055" />')
    svg_lines.append('      <stop offset="80%" stop-color="#A855F7" />')
    svg_lines.append('      <stop offset="100%" stop-color="#7928CA" />')
    svg_lines.append('    </linearGradient>')
    svg_lines.append('    <pattern id="scanlines" width="100" height="4" patternUnits="userSpaceOnUse">')
    svg_lines.append('      <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-width="1.2" opacity="0.32" />')
    svg_lines.append('    </pattern>')
    svg_lines.append('    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">')
    svg_lines.append('      <feGaussianBlur stdDeviation="1.8" result="blur" />')
    svg_lines.append('      <feMerge>')
    svg_lines.append('        <feMergeNode in="blur" />')
    svg_lines.append('        <feMergeNode in="SourceGraphic" />')
    svg_lines.append('      </feMerge>')
    svg_lines.append('    </filter>')
    svg_lines.append('  </defs>')
    svg_lines.append('  <style>')
    svg_lines.append('    .bg { fill: url(#spaceVignette); }')
    svg_lines.append('    .ascii-text {')
    svg_lines.append('      font-family: "Courier New", "Fira Code", monospace;')
    svg_lines.append('      font-weight: 700;')
    svg_lines.append('      letter-spacing: 0.5px;')
    svg_lines.append('      user-select: none;')
    svg_lines.append('    }')
    svg_lines.append('    .hud-circle {')
    svg_lines.append('      fill: none;')
    svg_lines.append('      stroke-dasharray: 6 12;')
    svg_lines.append('      animation: rotateHud 32s linear infinite;')
    svg_lines.append('      transform-origin: center;')
    svg_lines.append('    }')
    svg_lines.append('    .hud-circle-rev {')
    svg_lines.append('      fill: none;')
    svg_lines.append('      stroke-dasharray: 4 10;')
    svg_lines.append('      animation: rotateHudRev 22s linear infinite;')
    svg_lines.append('      transform-origin: center;')
    svg_lines.append('    }')
    svg_lines.append('    @keyframes rotateHud { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }')
    svg_lines.append('    @keyframes rotateHudRev { from { transform: rotate(360deg); } to { transform: rotate(0deg); } }')
    svg_lines.append('  </style>')
    svg_lines.append('  <!-- Fondo retro-futurista -->')
    svg_lines.append('  <rect width="500" height="500" rx="16" class="bg" />')
    svg_lines.append('  <!-- Anillos Cyber HUD de fondo -->')
    svg_lines.append('  <circle cx="250" cy="235" r="218" class="hud-circle" stroke="#7928CA" stroke-width="1.2" opacity="0.32" />')
    svg_lines.append('  <circle cx="250" cy="235" r="202" class="hud-circle-rev" stroke="#E11D48" stroke-width="1" opacity="0.28" />')
    svg_lines.append('  <circle cx="250" cy="235" r="230" stroke="#30363D" stroke-width="0.75" opacity="0.4" />')
    svg_lines.append('  <!-- Miras de calibración en esquinas -->')
    svg_lines.append('  <g opacity="0.45" stroke-width="1">')
    svg_lines.append('    <path d="M 22 36 L 22 22 L 36 22" stroke="#E11D48" fill="none" />')
    svg_lines.append('    <path d="M 478 36 L 478 22 L 464 22" stroke="#A855F7" fill="none" />')
    svg_lines.append('    <path d="M 22 464 L 22 478 L 36 478" stroke="#A855F7" fill="none" />')
    svg_lines.append('    <path d="M 478 464 L 478 478 L 464 478" stroke="#E11D48" fill="none" />')
    svg_lines.append('  </g>')
    svg_lines.append('  <!-- Matriz de Caracteres ASCII de Alta Definición -->')
    svg_lines.append('  <g class="ascii-text" filter="url(#neonGlow)">')

    for y in range(rows):
        row_y = margin_y + (y * step_y)
        row_str = ""
        for x in range(cols):
            val = pixels[x, y]
            idx = int((val / 256.0) * num_levels)
            idx = min(idx, num_levels - 1)
            char = ramp[idx]
            row_str += char
            
        ratio = y / float(rows)
        if ratio < 0.32:
            color = "#E11D48" # Neon red
        elif ratio < 0.68:
            color = "#FF0055" # Crimson neon
        else:
            color = "#A855F7" # Cyber Purple
            
        escaped_str = html.escape(row_str).replace(' ', '&#160;')
        svg_lines.append(f'    <text x="{box_size/2}" y="{row_y:.2f}" text-anchor="middle" font-size="{font_size:.2f}" fill="{color}" opacity="0.94">{escaped_str}</text>')

    svg_lines.append('  </g>')
    svg_lines.append('  <!-- Líneas de monitor CRT / Scanlines -->')
    svg_lines.append('  <rect width="500" height="500" rx="16" fill="url(#scanlines)" pointer-events="none" />')
    svg_lines.append('  <!-- HUD Status Footer -->')
    svg_lines.append('  <g transform="translate(0, 466)">')
    svg_lines.append('    <circle cx="150" cy="0" r="3.5" fill="#00FF66" />')
    svg_lines.append('    <text x="162" y="3.5" font-family="\'Fira Code\', monospace" font-size="10" font-weight="700" fill="#00FF66" letter-spacing="1">ONLINE</text>')
    svg_lines.append('    <text x="250" y="3.5" text-anchor="middle" font-family="\'Fira Code\', monospace" font-size="10" font-weight="600" fill="#8B949E" letter-spacing="2">EDGAR RAMOS // UNAC</text>')
    svg_lines.append('    <text x="350" y="3.5" font-family="\'Fira Code\', monospace" font-size="9" fill="#E11D48" letter-spacing="1">ARCHITECT</text>')
    svg_lines.append('  </g>')
    svg_lines.append('</svg>')

    with open(output_svg_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg_lines))
    print(f"SVG ASCII generado exitosamente en: {output_svg_path}")

if __name__ == "__main__":
    generate_ascii_svg('assets/github_photo.png', 'assets/avatar-ascii.svg', cols=64, rows=60)
