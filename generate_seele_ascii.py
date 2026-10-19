import html
from PIL import Image

def generate_seele_ascii_svg():
    im = Image.open('assets/seele_processed.png')
    
    # Grid configuration
    cols = 70
    rows = 54
    small = im.resize((cols, rows), Image.Resampling.LANCZOS)
    pix = small.load()
    
    box_w = 540
    box_h = 520
    margin_x = 24
    margin_y = 44
    
    step_y = (box_h - margin_y - 40) / rows
    font_size = step_y * 1.12
    
    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 520" width="100%" height="100%">')
    svg.append('  <defs>')
    svg.append('    <radialGradient id="seeleBg" cx="50%" cy="50%" r="70%">')
    svg.append('      <stop offset="0%" stop-color="#180A26" />')
    svg.append('      <stop offset="55%" stop-color="#0D1117" />')
    svg.append('      <stop offset="100%" stop-color="#05070B" />')
    svg.append('    </radialGradient>')
    svg.append('    <pattern id="crt" width="100" height="4" patternUnits="userSpaceOnUse">')
    svg.append('      <line x1="0" y1="0" x2="100" y2="0" stroke="#000000" stroke-width="1.2" opacity="0.28" />')
    svg.append('    </pattern>')
    svg.append('    <filter id="seeleGlow" x="-20%" y="-20%" width="140%" height="140%">')
    svg.append('      <feGaussianBlur stdDeviation="1.5" result="blur" />')
    svg.append('      <feMerge>')
    svg.append('        <feMergeNode in="blur" />')
    svg.append('        <feMergeNode in="SourceGraphic" />')
    svg.append('      </feMerge>')
    svg.append('    </filter>')
    svg.append('  </defs>')
    svg.append('  <style>')
    svg.append('    .bg { fill: url(#seeleBg); }')
    svg.append('    .ascii-text {')
    svg.append('      font-family: "Courier New", "Fira Code", monospace;')
    svg.append('      font-weight: 700;')
    svg.append('      letter-spacing: 0.5px;')
    svg.append('      user-select: none;')
    svg.append('    }')
    svg.append('    .hud-ring {')
    svg.append('      fill: none;')
    svg.append('      stroke-dasharray: 6 14;')
    svg.append('      animation: rotClock 36s linear infinite;')
    svg.append('      transform-origin: center;')
    svg.append('    }')
    svg.append('    .hud-ring-rev {')
    svg.append('      fill: none;')
    svg.append('      stroke-dasharray: 4 10;')
    svg.append('      animation: rotCounter 26s linear infinite;')
    svg.append('      transform-origin: center;')
    svg.append('    }')
    svg.append('    @keyframes rotClock { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }')
    svg.append('    @keyframes rotCounter { from { transform: rotate(360deg); } to { transform: rotate(0deg); } }')
    svg.append('  </style>')
    svg.append('  <rect width="540" height="520" rx="16" class="bg" />')
    svg.append('  <circle cx="270" cy="240" r="230" class="hud-ring" stroke="#7928CA" stroke-width="1.2" opacity="0.35" />')
    svg.append('  <circle cx="270" cy="240" r="214" class="hud-ring-rev" stroke="#E11D48" stroke-width="1" opacity="0.3" />')
    svg.append('  <circle cx="270" cy="240" r="244" stroke="#30363D" stroke-width="0.8" opacity="0.4" />')
    
    # Corner brackets
    svg.append('  <g opacity="0.6" stroke-width="1.2">')
    svg.append('    <path d="M 20 34 L 20 20 L 34 20" stroke="#E11D48" fill="none" />')
    svg.append('    <path d="M 520 34 L 520 20 L 506 20" stroke="#A855F7" fill="none" />')
    svg.append('    <path d="M 20 486 L 20 500 L 34 500" stroke="#A855F7" fill="none" />')
    svg.append('    <path d="M 520 486 L 520 500 L 506 500" stroke="#E11D48" fill="none" />')
    svg.append('  </g>')
    
    # ASCII group
    svg.append('  <g class="ascii-text" filter="url(#seeleGlow)">')
    
    body_ramp = ['.', ':', '-', '+']
    bright_ramp = ['=', '*', '%', '#', '@', '█']
    
    for y in range(rows):
        row_y = margin_y + (y * step_y)
        row_chars = []
        for x in range(cols):
            v = pix[x, y]
            if v < 28:
                row_chars.append(' ')
            elif v < 130:
                b_idx = int(((v - 28) / (130 - 28)) * len(body_ramp))
                row_chars.append(body_ramp[min(b_idx, len(body_ramp)-1)])
            else:
                br_idx = int(((v - 130) / (256 - 130)) * len(bright_ramp))
                row_chars.append(bright_ramp[min(br_idx, len(bright_ramp)-1)])
        
        row_str = ''.join(row_chars)
        ratio = y / float(rows)
        if ratio < 0.35:
            color = "#FF2A6D"
        elif ratio < 0.70:
            color = "#F43F5E"
        else:
            color = "#C084FC"
            
        esc = html.escape(row_str).replace(' ', '&#160;')
        svg.append(f'    <text x="{box_w/2}" y="{row_y:.2f}" text-anchor="middle" font-size="{font_size:.2f}" fill="{color}" opacity="0.95">{esc}</text>')
        
    svg.append('  </g>')
    svg.append('  <rect width="540" height="520" rx="16" fill="url(#crt)" pointer-events="none" />')
    
    # Header & Footer HUD label
    svg.append('  <g transform="translate(0, 30)">')
    svg.append('    <text x="30" y="0" font-family="\'Fira Code\', monospace" font-size="9" font-weight="700" fill="#E11D48" letter-spacing="1.5">// SEELE_PROTOCOL_01</text>')
    svg.append('    <text x="510" y="0" text-anchor="end" font-family="\'Fira Code\', monospace" font-size="9" font-weight="600" fill="#8B949E" letter-spacing="1">SEVEN_EYES_COUNCIL</text>')
    svg.append('  </g>')
    svg.append('  <g transform="translate(0, 495)">')
    svg.append('    <circle cx="140" cy="0" r="3.5" fill="#00FF66" />')
    svg.append('    <text x="152" y="3.5" font-family="\'Fira Code\', monospace" font-size="10" font-weight="700" fill="#00FF66" letter-spacing="1">ONLINE</text>')
    svg.append('    <text x="270" y="3.5" text-anchor="middle" font-family="\'Fira Code\', monospace" font-size="10" font-weight="600" fill="#8B949E" letter-spacing="2">EDGAR RAMOS // UNAC</text>')
    svg.append('    <text x="400" y="3.5" font-family="\'Fira Code\', monospace" font-size="9" font-weight="700" fill="#A855F7" letter-spacing="1">ARCHITECT</text>')
    svg.append('  </g>')
    svg.append('</svg>')
    
    with open('assets/seele-ascii.svg', 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    with open('assets/avatar-ascii.svg', 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print('Seele SVG generated successfully!')

if __name__ == '__main__':
    generate_seele_ascii_svg()
