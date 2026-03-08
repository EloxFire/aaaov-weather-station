# =========
# SATTION METEO AAAOV
# wind.py
# Fichier de controle globale du vent :)
# Controle de l'anémomètre et de la girouette.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

from time import sleep

import RPi.GPIO as GPIO
import time

print("Init wind sensor...")
# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Use GPIO 5, pull-down resistor

count = 0

def count_pulse(channel):
    global count
    count += 1
    print(f"Pulse count: {count}")

# Add event detection on rising edge (switch opens)
GPIO.add_event_detect(5, GPIO.RISING, callback=count_pulse, bouncetime=50)

try:
    while True:
        time.sleep(1)  # Keep script running
except KeyboardInterrupt:
    print(f"Final count: {count}")
    GPIO.cleanup()