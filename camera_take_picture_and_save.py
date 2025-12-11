# Importieren der Bibliotheken 
from picamera2 import Picamera2                     # um auf die Pi Camera M12 zuzugreigfen (sicherer als cv2)
from datetime import datetime                       # um auf die aktuelle Tageszeit zuzugreifen 
import os

# Verzeichnis, in das gespeichert werden soll
save_directory = "/home/raspi01/Dokumente/Fernerkundung_Wolkenkamera/Wolkenbilder"

# Verzeichnis erstellen, falls nicht vorhanden
os.makedirs(save_directory, exist_ok=True)

# Zeitstempel erzeugen
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"Wolkenbild{timestamp}.jpg"
filepath = os.path.join(save_directory, filename)

# Kamera initialisieren
picam = Picamera2()
config = picam.create_still_configuration()
picam.configure(config)

# Bild mit der Kamera aufnehmen 
picam.start()
picam.capture_file(filepath)
picam.stop()

