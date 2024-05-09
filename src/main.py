import time
import RPi.GPIO as GPIO
import board
import adafruit_dht
import math
from w1thermsensor import W1ThermSensor

class Sensors:
    dht11 = adafruit_dht.DHT11(board.D14,use_pulseio=True)
    waterSensor = W1ThermSensor()
    GPIO.setmode(GPIO.BCM)
    PIN_AIRPUMP = 21
    PIN_TEMP = 20
    PIN_FAN = 16
    GPIO.setup(PIN_AIRPUMP, GPIO.OUT)
    GPIO.setup(PIN_TEMP, GPIO.OUT)
    GPIO.setup(PIN_FAN, GPIO.OUT)
    def __init__(self):
        pass
    def getSoilTemp(self):
        while True:
            try:
                temperature_c = self.dht11.temperature
                return(str(temperature_c))
            except RuntimeError as error:
                time.sleep(2.0)
                continue
            except Exception as error:
                self.dht11.exit()
    def getSoilHumidity(self):
        while True:
            try:
                humidity = self.dht11.humidity
                return(str(humidity))
            except RuntimeError as error:
                time.sleep(2.0)
                continue
            except Exception as error:
                self.dht11.exit()
    def getWaterTemp(self):
        return(int(self.waterSensor.get_temperature()))
    def toggleFan(self):
         GPIO.output(self.PIN_FAN, abs(GPIO.input(self.PIN_FAN)-1))
    def toggleTemp(self):
        GPIO.output(self.PIN_TEMP, abs(GPIO.input(self.PIN_TEMP)-1))
    def toggleAir(self):
        GPIO.output(self.PIN_AIRPUMP, abs(GPIO.input(self.PIN_AIRPUMP)-1))
if __name__ == "__main__":
    app = Sensors()
