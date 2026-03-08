# =========
# STATION METEO AAAOV
# dht11.py
# Lecture température / humidité du capteur DHT11
# =========

import board
import adafruit_dht

print("Init DHT11 sensor...")
dht_sensor = adafruit_dht.DHT11(board.D4)
print("DHT11 sensor initialized.")

temp = None
humidity = None


def read():
    global temp, humidity

    try:
        temp = dht_sensor.temperature
        humidity = dht_sensor.humidity
    except RuntimeError as e:
        print("DHT11 error: {}".format(e))

    return temp, humidity