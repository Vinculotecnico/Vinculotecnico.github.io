import glob
import re

files = glob.glob('*.html')
tooltips = {
    'Nosotros': 'Conoce sobre nuestra propuesta de valor para tu negocio.',
    'Modelo': 'Conoce sobre nuestros pilares y bases técnicas.',
    'Servicios': 'Conoce sobre nuestras soluciones.'
}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's just directly replace the <li><a href="X.html">Text</a></li>
    for link_text, tooltip_text in tooltips.items():
        # Clean any existing tooltips for this link text in the header nav
        # To be safe we just replace the whole anchor tag inside the nav block
        target_a = f'> {link_text}</a>' # just in case of spaces
        
        # Simpler approach:
        # 1. find <a href="nosotros.html">Nosotros</a>
        # replace with <a href="nosotros.html" data-tooltip="...">Nosotros</a>
        
        # Remove old ones
        content = re.sub(r' data-tooltip="[^"]*"', '', content)
        
    # Re-apply correctly
    for link_text, tooltip_text in tooltips.items():
        # Match <a href="something.html">LinkText</a>
        pattern = r'<a href="([^"]+)">' + link_text + r'</a>'
        replacement = f'<a href="\\1" data-tooltip="{tooltip_text}">{link_text}</a>'
        content = re.sub(pattern, replacement, content)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Fixed tooltips in {f}')
