import os
import glob

files = glob.glob('*.html')
for f in files:
    if f == 'modelo.html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if already added
    if '<li><a href="modelo.html">Modelo</a></li>' not in content:
        # Replace in Main Nav and Footer
        content = content.replace(
            '<li><a href="nosotros.html">Nosotros</a></li>',
            '<li><a href="nosotros.html">Nosotros</a></li>\n          <li><a href="modelo.html">Modelo</a></li>'
        )
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
