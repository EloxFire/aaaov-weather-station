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