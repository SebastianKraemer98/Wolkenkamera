from picamera2 import Picamera2
from datetime import datetime, timedelta
import os
import time

# --- Einstellungen ---
BASE_DIR = "/home/raspi01/Dokumente/Fernerkundung_Wolkenkamera/Wolkenbilder"

os.makedirs(BASE_DIR, exist_ok=True)

# Kamera initialisieren
picam = Picamera2()
config = picam.create_still_configuration()
picam.configure(config)
picam.start()

print("Wolkenkamera gestartet. Drücke STRG+C zum Beenden.")

def sleep_until_next_full_minute():
    now = datetime.now()
    next_minute = (now.replace(second=0, microsecond=0) + timedelta(minutes=1))
    seconds_to_wait = (next_minute - now).total_seconds()
    time.sleep(seconds_to_wait)

try:
    # zuerst auf den nächsten Minutenbeginn synchronisieren
    sleep_until_next_full_minute()

    while True:
        now = datetime.now()  # sollte hier praktisch immer xx:xx:00 sein

        # Tagesordner
        day_folder = now.strftime("%Y-%m-%d")
        save_directory = os.path.join(BASE_DIR, day_folder)
        os.makedirs(save_directory, exist_ok=True)

        # Dateiname
        timestamp = now.strftime("%H-%M-%S")
        filename = f"Wolkenbild_{timestamp}.png"
        filepath = os.path.join(save_directory, filename)

        # Bild aufnehmen
        picam.capture_file(filepath)
        print("Gespeichert:", filepath)

        # bis zur nächsten vollen Minute warten
        sleep_until_next_full_minute()

except KeyboardInterrupt:
    print("\nAufnahme manuell abgebrochen.")

finally:
    picam.stop()
    picam.close()
    print("Kamera gestoppt.")
