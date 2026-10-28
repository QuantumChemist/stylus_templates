import os
from urllib.request import urlopen

github_url = "https://raw.githubusercontent.com/QuantumChemist/stylus_templates/refs/heads/main/uwu_helper.py"

with urlopen(github_url) as response:
    code_inhalt = response.read().decode('utf-8')

cache_dir = os.path.expanduser('~/.cache')
os.makedirs(cache_dir, exist_ok=True)
with open(os.path.join(cache_dir, 'uwu_helper.py'), 'w', encoding='utf-8') as f:
    f.write(code_inhalt)

startup_dir = get_ipython().profile_dir.startup_dir
with open(os.path.join(startup_dir, '00-uwu-path.py'), 'w', encoding='utf-8') as f:
    f.write("import sys, os; sys.path.append(os.path.expanduser('~/.cache'))\n")

print("🎉 UPDATE ERFOLGREICH! Christina, dein System ist jetzt vollautomatisch und kapitelsicher! 🎉")
