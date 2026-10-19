def generate_terminal_svg(output_path="assets/terminal-console.svg"):
    # SVG terminal clean, retro-cyber aesthetic
    # Width: 780, Height: 230
    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 230" width="100%" height="100%">')
    svg.append('  <defs>')
    svg.append('    <linearGradient id="termBg" x1="0%" y1="0%" x2="100%" y2="100%">')
    svg.append('      <stop offset="0%" stop-color="#11151D" />')
    svg.append('      <stop offset="100%" stop-color="#0A0D14" />')
    svg.append('    </linearGradient>')
    svg.append('    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="0%">')
    svg.append('      <stop offset="0%" stop-color="#FF0055" />')
    svg.append('      <stop offset="50%" stop-color="#A855F7" />')
    svg.append('      <stop offset="100%" stop-color="#00FF66" />')
    svg.append('    </linearGradient>')
    svg.append('  </defs>')
    svg.append('  <style>')
    svg.append('    .term-code { font-family: "Fira Code", "Courier New", monospace; font-size: 13px; }')
    svg.append('    .prompt { fill: #00FF66; font-weight: 700; }')
    svg.append('    .cmd { fill: #F43F5E; font-weight: 700; }')
    svg.append('    .title-val { fill: #FFFFFF; font-weight: 600; }')
    svg.append('    .sub-val { fill: #A855F7; font-weight: 600; }')
    svg.append('    .fiis-val { fill: #38BDF8; font-weight: 600; }')
    svg.append('    .branch { fill: #8B949E; }')
    svg.append('    .key { fill: #FF0055; font-weight: 600; }')
    svg.append('    .val { fill: #E6EDF3; }')
    svg.append('    .cursor { fill: #00FF66; animation: blink 1s step-end infinite; }')
    svg.append('    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }')
    svg.append('  </style>')
    
    # Outer frame
    svg.append('  <rect x="1" y="1" width="778" height="228" rx="10" fill="url(#termBg)" stroke="#30363D" stroke-width="1.2" />')
    svg.append('  <rect x="1" y="1" width="778" height="34" rx="10" fill="#161B22" />')
    svg.append('  <rect x="1" y="24" width="778" height="11" fill="#161B22" />')
    svg.append('  <line x1="1" y1="35" x2="779" y2="35" stroke="url(#borderGrad)" stroke-width="1.5" opacity="0.8" />')
    
    # Window controls
    svg.append('  <circle cx="20" cy="18" r="5" fill="#FF5F56" />')
    svg.append('  <circle cx="36" cy="18" r="5" fill="#FFBD2E" />')
    svg.append('  <circle cx="52" cy="18" r="5" fill="#27C93F" />')
    svg.append('  <text x="390" y="22" text-anchor="middle" font-family="\'Fira Code\', monospace" font-size="11" fill="#8B949E" font-weight="600">tiburonchin@fiis-unac: ~ (zsh)</text>')
    
    # Terminal content
    svg.append('  <g class="term-code" transform="translate(24, 62)">')
    
    # Line 1: whoami
    svg.append('    <text x="0" y="0"><tspan class="prompt">❯ </tspan><tspan class="cmd">whoami</tspan></text>')
    # Line 2: identity with FIIS / Sistemas 7mo ciclo
    svg.append('    <text x="18" y="22"><tspan class="title-val">Edgar Ramos Trujillo</tspan> <tspan class="branch">|</tspan> <tspan class="fiis-val">Ingeniería de Sistemas (7mo Ciclo - FIIS UNAC)</tspan></text>')
    
    # Line 3: core_specialties
    svg.append('    <text x="0" y="56"><tspan class="prompt">❯ </tspan><tspan class="cmd">core_specialties</tspan></text>')
    # Line 4: Autonomous agents
    svg.append('    <text x="18" y="78"><tspan class="branch">├── </tspan><tspan class="key">Autonomous AI Agents : </tspan><tspan class="val">FastMCP, Model Context Protocol, LLM Orchestration</tspan></text>')
    # Line 5: Backend
    svg.append('    <text x="18" y="98"><tspan class="branch">├── </tspan><tspan class="key">Backend &amp; Pipelines  : </tspan><tspan class="val">Python (FastAPI/Scrapy), TypeScript (Node/Next), Supabase RLS</tspan></text>')
    # Line 6: Infra
    svg.append('    <text x="18" y="118"><tspan class="branch">└── </tspan><tspan class="key">Cloud &amp; Web Systems  : </tspan><tspan class="val">Docker, WebRTC SFU, Arquitectura de Sistemas &amp; CI/CD</tspan></text>')
    
    # Line 7: cursor
    svg.append('    <text x="0" y="146"><tspan class="prompt">❯ </tspan><rect x="18" y="134" width="8" height="15" class="cursor" /></text>')
    
    svg.append('  </g>')
    svg.append('</svg>')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f'Terminal SVG generated in {output_path}')

if __name__ == '__main__':
    generate_terminal_svg()
