from time import sleep

import dht11
import bme280
import rainfall
import wind


def main():
    wind.main()
    rainfall.main()

    while True:
        temp, humidity = dht11.read()
        bme_temp = bme280.read()
        wind_speed = wind.read()
        rain_amount = rainfall.read()

        print("Temperature: {}°C".format(temp))
        print("Humidity: {}%".format(humidity))
        print("BME280 Temperature: {}°C".format(bme_temp))
        print("Rainfall: {} mm".format(rain_amount))
        print("Wind speed: {} km/h".format(wind_speed))

        sleep(2)


if __name__ == "__main__":
    main()