# =========
# SATTION METEO AAAOV
# dht11.py
# Ce fichier permet de lire les valeurs de température et d'humidité du capteur DHT11
# =========

import board
import adafruit_dht
from time import sleep

dht_sensor = adafruit_dht.DHT11(board.D4)

while True :
  try: 
    temp = dht_sensor.temperature
    humidity = dht_sensor.humidity
    print("Temperature: {}°C".format(temp))
    print("Humidity: {}%".format(humidity))
  except RuntimeError as e :
    print("Error: {}".format(e))

  sleep(2)