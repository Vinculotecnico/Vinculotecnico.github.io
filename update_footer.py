import os
import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We only want to replace inside the footer.
    # The block looks like:
    # <h4>Compañía</h4>
    # <ul>
    #   <li><a href="nosotros.html">Nosotros</a></li>
    
    target_pattern = r'(<h4>Compa\u00f1\u00eda</h4>\s*<ul>\s*)<li><a href="nosotros\.html">Nosotros</a></li>'
    # We'll use re to substitute. \u00f1 is ñ
    if re.search(target_pattern, content):
        new_content = re.sub(target_pattern, r'\1<li><a href="index.html">Inicio</a></li>\n          <li><a href="nosotros.html">Nosotros</a></li>', content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
    else:
        # Also try to match with normal ñ just in case
        target_pattern2 = r'(<h4>Compañía</h4>\s*<ul>\s*)<li><a href="nosotros\.html">Nosotros</a></li>'
        if re.search(target_pattern2, content):
            new_content = re.sub(target_pattern2, r'\1<li><a href="index.html">Inicio</a></li>\n          <li><a href="nosotros.html">Nosotros</a></li>', content)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')
