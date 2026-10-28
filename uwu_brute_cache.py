import os

cache_path = os.path.expanduser('~/.cache/uwu_helper.py')
code_direkt = """import json
import os
from IPython import get_ipython

def lade(wunsch_zelle, loesungs_datei):
    wunsch_zelle -= 1
    loesungs_datei += '-solution.ipynb'
    
    aktueller_ordner = os.getcwd()
    loesungs_pfad_ordner = aktueller_ordner + "-solutions"
    
    loesungs_pfad = os.path.join(loesungs_pfad_ordner, loesungs_datei)
    
    if not os.path.exists(loesungs_pfad):
        print(f"❌ Die Datei '{loesungs_datei}' existiert nicht im Ordner '{os.path.basename(loesungs_pfad_ordner)}'.")
        return

    with open(loesungs_pfad, "r", encoding="utf-8") as file:
        notebook_daten = json.load(file)
    
    code_zellen = [z for z in notebook_daten.get("cells", []) if z.get("cell_type") == "code" and "".join(z.get("source", [])) != ""]
    
    if 0 <= wunsch_zelle < len(code_zellen):
        ziel_code = "".join(code_zellen[wunsch_zelle].get("source", []))
        get_ipython().set_next_input(ziel_code, replace=True)
        print(f"✨ Lösung für lila Zelle Nummer {wunsch_zelle + 1} wurde eingefügt! ✨")
    else:
        print(f"❌ Nummer {wunsch_zelle + 1} gibt es in dieser Lösung nicht.")
"""

with open(cache_path, 'w', encoding='utf-8') as f:
    f.write(code_direkt)

print("🎯 BOOM! Der Server MUSS jetzt deine neue Version benutzen!")
