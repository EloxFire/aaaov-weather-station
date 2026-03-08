# =========
# STATION METEO AAAOV
# rainfall.py
# Controle du pluviomètre
# =========

from gpiozero import Button

bucket_size = 0.2794   # mm de pluie par basculement
count = 0              # nombre de basculements
rain_sensor = None


def bucket_tipped():
    global count
    count += 1
    print("Rain bucket tipped. Total count:", count)


def calculate_rainfall():
    global count
    return round(count * bucket_size, 4)


def reset_rainfall():
    global count
    count = 0


def main():
    global rain_sensor

    if rain_sensor is None:
        print("Init rain sensor...")
        rain_sensor = Button(6, pull_up=True, bounce_time=0.01)
        rain_sensor.when_pressed = bucket_tipped
        print("Rain sensor initialized.")


def read():
    return calculate_rainfall()