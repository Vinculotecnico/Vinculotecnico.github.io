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
    
    # We only want to apply this to the header navigation, which is within <nav class="main-nav">
    # Because there might be mobile nav or footer nav, we find the <nav class="main-nav"> block
    nav_match = re.search(r'<nav class="main-nav">(.*?)</nav>', content, re.DOTALL)
    if nav_match:
        nav_content = nav_match.group(1)
        original_nav = nav_content
        
        for link_text, tooltip_text in tooltips.items():
            # Matches: <a href="nosotros.html">Nosotros</a>
            # and we want to turn it into <a href="nosotros.html" data-tooltip="...">Nosotros</a>
            
            # Remove any existing data-tooltip just in case to prevent duplicates
            nav_content = re.sub(r' data-tooltip="[^"]*"', '', nav_content)
            
            # Now add it
            pattern = r'(<a href="[^"]*?")(>{})'.format(link_text)
            replacement = r'\1 data-tooltip="{}"\2'.format(tooltip_text)
            nav_content = re.sub(pattern, replacement, nav_content)
            
        if original_nav != nav_content:
            content = content.replace(original_nav, nav_content)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f'Added tooltips to {f}')
