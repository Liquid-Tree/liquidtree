import time
import board
import adafruit_dht
from w1thermsensor import W1ThermSensor

class Sensors:
    def __init__(self):
        self.dht11 = adafruit_dht.DHT11(board.D14,use_pulseio=True)
        self.waterSensor = W1ThermSensor()
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
        return(self.waterSensor.get_temperature())

if __name__ == "__main__":
    app = Sensors()
    #print(app.getSoilTemp())
    #print(app.getSoilHumidity())
    print(app.getWaterTemp())
