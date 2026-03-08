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
    while True:
        dht_temp, dht_humidity = dht11.read()
        bme_temp = bme280.read_temperature()
        wind_speed = wind.read_speed()
        rain_count = rainfall.read_count()

        print(f"Temperature: {dht_temp}°C")
        print(f"Humidity: {dht_humidity}%")
        print(f"BME280 Temperature: {bme_temp}°C")
        print(f"Rainfall count: {rain_count}")
        print(f"Wind speed: {wind_speed}")

        sleep(2)


if __name__ == "__main__":
    main()