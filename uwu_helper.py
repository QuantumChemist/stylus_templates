import json
import os
from IPython import get_ipython

def lade(wunsch_zelle - 1, loesungs_datei):
    aktueller_ordner = os.getcwd()
    basis_ordner = os.path.dirname(aktueller_ordner) 
    
    loesungs_ordner_name = next((f for f in os.listdir(basis_ordner) if f.endswith("-solutions")), None)
    
    if not loesungs_ordner_name:
        print("❌ Kein Lösungsordner für dieses Modul im Verzeichnis gefunden.")
        return
        
    loesungs_pfad = os.path.join(basis_ordner, loesungs_ordner_name, loesungs_datei)
    
    if not os.path.exists(loesungs_pfad):
        print(f"❌ Die Datei '{loesungs_datei}' existiert nicht im Ordner '{loesungs_ordner_name}'.")
        return

    with open(loesungs_pfad, "r", encoding="utf-8") as file:
        notebook_daten = json.load(file)
    
    code_zellen = [z for z in notebook_daten.get("cells", []) if z.get("cell_type") == "code" and "".join(z.get("source", [])).strip()]
    
    if 0 <= wwunsch_zelle < len(code_zellen):
        ziel_code = "".join(code_zellen[wunsch_zelle].get("source", []))
        get_ipython().set_next_input(ziel_code, replace=False)
        print(f"✨ Lösung für lila Zelle Nummer {wunsch_zelle} wurde eingefügt! ✨")
    else:
        print(f"❌ Nummer {wunsch_zelle} gibt es in dieser Lösung nicht.")
