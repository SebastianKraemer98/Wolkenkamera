# Importieren der Bibliotheken 
from picamera2 import Picamera2
from datetime import datetime
import os
import time

# --- Einstellungen ---
BASE_DIR = "/home/raspi01/Dokumente/Fernerkundung_Wolkenkamera/Wolkenbilder"
INTERVAL_SECONDS = 30                                                              # alle 30 Sekunden ein bild

# Basisverzeichnis erstellen, falls nicht vorhanden
os.makedirs(BASE_DIR, exist_ok=True)

# Kamera initialisieren
picam = Picamera2()
config = picam.create_still_configuration()
picam.configure(config)
picam.start()

print("Wolkenkamera gestartet. Drücke STRG+C zum Beenden.")

try:
    while True:
        now = datetime.now()

        # Tagesordner: z.B. 2025-01-24
        day_folder = now.strftime("%Y-%m-%d")
        save_directory = os.path.join(BASE_DIR, day_folder)
        os.makedirs(save_directory, exist_ok=True)

        # Dateiname: z.B. Wolkenbild_15-32-10.jpg
        timestamp = now.strftime("%H-%M-%S")
        filename = f"Wolkenbild_{timestamp}.jpg"
        filepath = os.path.join(save_directory, filename)

        # Bild aufnehmen
        picam.capture_file(filepath)
        print("Gespeichert:", filepath)

        # Warten bis zur nächsten Aufnahme
        time.sleep(INTERVAL_SECONDS)

except KeyboardInterrupt:
    print("\nAufnahme manuell abgebrochen.")

finally:
    picam.stop()
    picam.close()
    print("Kamera gestoppt.")