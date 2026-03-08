# =========
# SATTION METEO - AAAOV
# main.py
# Fichier principal du programme de lecture des données de la Station météo.
# Enzo Avagliano - contact@enzoavagliano.fr
# Contact AAAOV : contact@aaaov.fr
# =========

import dht11


def main():
    dht11.main()

    print("Temperature: {}°C".format(dht11.temp))
    print("Humidity: {}%".format(dht11.humidity))

if __name__ == "__main__":
    print("=== STATION MÉTÉO - AAAOV ===")
    print("Initialisation...")
    main()