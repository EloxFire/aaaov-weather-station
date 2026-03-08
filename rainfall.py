# =========
# SATTION METEO AAAOV
# rainfall.py
# Fichier de controle global de la pluie :)
# Controle du pluviomètre.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

from gpiozero import Button

bucket_size = 0.2794
count = 0

def bucket_tipped():
  global count
  count = count + 1
  print("Rain bucket tipped. Total count:", count)

def reset_rainfall():
  global count
  count = 0

def calculate_rainfall():
  global count
  return count * bucket_size

print("Init rain sensor...")
rain_sensor = Button(6) 
rain_sensor.when_pressed = bucket_tipped
print("Rain sensor initialized.")