# =========
# STATION METEO AAAOV
# wind.py
# Contrôle de l'anémomètre
# =========

import math
from gpiozero import Button
from time import sleep

sensor_radius_cm = 9.0
read_interval = 5
wind_count = 0
adjustment_factor = 1.8
speed = 0.0

wind_sensor = None


def spin():
    global wind_count
    wind_count += 1


def calculate_wind_speed(interval):
    circumference_cm = 2 * math.pi * sensor_radius_cm
    rotations_per_sec = (wind_count / 2) / interval
    cup_distance_cm_per_sec = circumference_cm * rotations_per_sec
    wind_speed = (cup_distance_cm_per_sec / 100) * 3.6
    return round(wind_speed * adjustment_factor, 2)


def reset_wind():
    global wind_count
    wind_count = 0


def main():
    global wind_sensor

    if wind_sensor is None:
        print("Init anemometer...")
        wind_sensor = Button(5, pull_up=True, bounce_time=0.005)
        wind_sensor.when_pressed = spin
        print("Anemometer initialized.")


def read():
    global speed

    if wind_sensor is None:
        main()

    reset_wind()
    sleep(read_interval)
    speed = calculate_wind_speed(read_interval)
    return speed