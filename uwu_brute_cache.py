import os
import sys
import shutil

cache_dir = os.path.expanduser('~/.cache')
cache_path = os.path.join(cache_dir, 'uwu_helper.py')

pycache_path = os.path.join(cache_dir, '__pycache__')
if os.path.exists(pycache_path):
    shutil.rmtree(pycache_path)

# 🛠️ ERWEITERT: Jetz baut der Code auf deiner exakten Vorlage auf!
neuer_code = """import json
import os
from IPython import get_ipython
from IPython.display import display, HTML

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
        roh_code = "".join(code_zellen[wunsch_zelle].get("source", []))
        
        gesaeuberte_zeilen = []
        for zeile in roh_code.splitlines():
            if not zeile.strip().startswith('#'):
                gesaeuberte_zeilen.append(zeile)
                
        ziel_code = "\\n".join(gesaeuberte_zeilen)
        get_ipython().set_next_input(ziel_code, replace=True)
        
        # 🪄 DIE BRILANTE ANPASSUNG: Sucht genau den Ort des Aufrufs und holt den Fokus zurück!
        cursor_magic = '''
        <script>
            setTimeout(function() {
                // Findet exakt die Zelle, die gerade ersetzt wurde
                var currentScript = document.currentScript;
                var myCell = currentScript ? currentScript.closest('.jp-Cell') : null;
                
                if (myCell) {
                    // 1. Zwingt JupyterLab, diese Zelle visuell wieder auszuwählen
                    var inputArea = myCell.querySelector('.jp-Cell-inputArea');
                    if (inputArea) { inputArea.click(); }
                    
                    // 2. Setzt den blinkenden Cursor direkt in den Code-Editor
                    var editorArea = myCell.querySelector('.cm-content, .CodeMirror-code, [contenteditable="true"]');
                    if (editorArea) {
                        editorArea.focus();
                        var clickEvent = new MouseEvent('click', { bubbles: true, cancelable: true });
                        editorArea.dispatchEvent(clickEvent);
                    }
                }
            }, 100); // 100ms warten, damit Jupiters automatischer Sprung nach unten erst fertig ist
        </script>
        '''
        display(HTML(cursor_magic))
        
        print(f"✨ Lösung für lila Zelle Nummer {wunsch_zelle + 1} geladen! Drücke SHIFT + ENTER zum Ausführen! 🎯 ✨")
    else:
        print(f"❌ Nummer {wunsch_zelle + 1} gibt es in dieser Lösung nicht.")
"""

with open(cache_path, 'w', encoding='utf-8') as f:
    f.write(neuer_code)

if 'uwu_helper' in sys.modules:
    del sys.modules['uwu_helper']

import uwu_helper
print("--------------------------------------------------")
print(f"🎯 ERFOLG! Das Modul wird geladen aus: {uwu_helper.__file__}")
print("--------------------------------------------------")
