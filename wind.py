# =========
# SATTION METEO AAAOV
# wind.py
# Fichier de controle globale du vent :)
# Controle de l'anémomètre et de la girouette.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

from gpiozero import Button

wind_sensor = Button(5)
wind_count = 0

def spin():
  global wind_count
  wind_count = wind_count + 1
  print("Spin detected : " + str(wind_count))

wind_sensor.when_pressed = spin