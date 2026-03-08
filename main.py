# =========
# SATTION METEO - AAAOV
# main.py
# Fichier principal du programme de lecture des données de la Station météo.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

from time import sleep

import dht11
import bme280
import rainfall
import wind


def main():
    dht11.main()
    bme280.main()
    wind.main()
    rainfall.main()

    while True:
        print("Temperature: {}°C".format(dht11.temp))
        print("Humidity: {}%".format(dht11.humidity))
        print("BME280 Temperature: {}°C".format(bme280.T))

        print("Rainfall count: {}".format(rainfall.count))
        print("Wind speed : {}".format(wind.speed))
        sleep(2)

if __name__ == "__main__":
    print("=== STATION MÉTÉO - AAAOV ===")
    print("Initialisation...")
    main()