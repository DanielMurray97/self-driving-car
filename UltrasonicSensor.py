from easygopigo3 import EasyGoPiGo3
from time import sleep



GPG = EasyGoPiGo3()

port = "AD2"

sensor = GPG.init_ultrasonic_sensor(port)

sensor.set_safe_distance(127)#127 = 5 inches in mm

def inches():

    if sensor.is_too_close == True:
        return True
    else:
        return False



if __name__ == '__main__':
    while True:
        inches()


