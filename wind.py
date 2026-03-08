# =========
# SATTION METEO AAAOV
# wind.py
# Fichier de controle globale du vent :)
# Controle de l'anémomètre et de la girouette.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

from gpiozero import Button
from signal import pause
import time

pulse_count = 0
start_time = time.time()

# Reed switch entre GPIO 5 et GND
# pull_up=True par défaut
# bounce_time en secondes
anemometer = Button(5, pull_up=True, bounce_time=0.005)

def count_pulse():
    global pulse_count
    pulse_count += 1

anemometer.when_pressed = count_pulse

try:
    while True:
        time.sleep(5)
        elapsed = time.time() - start_time
        count = pulse_count

        # remise à zéro pour la fenêtre suivante
        pulse_count = 0
        start_time = time.time()

        freq_hz = count / elapsed
        print(f"Impulsions: {count} en {elapsed:.2f}s | fréquence: {freq_hz:.2f} Hz")

        # Exemple générique :
        # vitesse = freq_hz * FACTEUR_CAPTEUR
        # Remplace FACTEUR_CAPTEUR par la constante de ton modèle
except KeyboardInterrupt:
    pass