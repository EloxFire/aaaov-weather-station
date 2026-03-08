# =========
# SATTION METEO AAAOV
# wind.py
# Fichier de controle globale du vent :)
# Controle de l'anémomètre et de la girouette.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

import math
from gpiozero import Button
from time import sleep

sensor_radius_cm = 9.0 # Rayon du capteur en cm
read_interval = 5 # Intervale de mesure en s
wind_count = 0 # Nombre de demi-rotations
adjustment_factor = 1.8 # Facteur d'ajustement pour compenser l'energie perdue dans la rotation des bras
speed = 0.0 # Vitesse du vent en km/h

def spin():
  global wind_count
  wind_count = wind_count + 1

def calculate_wind_speed(interval):
  global wind_speed
  circumference_cm = 2 * math.pi * sensor_radius_cm
  rotations = wind_count / interval # Nombre de rotations dans l'intervale de mesure
  # Distance parcourue par une coupe
  cup_distance = circumference_cm * rotations
  # Calcul vitesse
  wind_speed = ((cup_distance / interval) / 100) * 3.6 # Convertion en km/h
  return round(wind_speed * adjustment_factor, 2)

def reset_wind():
  global wind_count
  wind_count = 0


print("Init anemometer...")
wind_sensor = Button(5)
wind_sensor.when_pressed = spin
print("Anemometer initialized.")

while True :
  reset_wind()
  sleep(read_interval)
  speed = calculate_wind_speed(read_interval)
#   print("Wind speed:", calculate_wind_speed(read_interval), "km/h")
  