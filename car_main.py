from easygopigo3 import EasyGoPiGo3
from curve_detection import get_lane_curve
import webcam
import Movement
from time import sleep

GPG = EasyGoPiGo3()

port = "AD2"

sensor = GPG.init_ultrasonic_sensor(port)

sensor.set_safe_distance(120)


def car_main():
    img_vid = webcam.get_vid(display=False)
    curve_val = get_lane_curve(img_vid, 0)

    sensitivity = 0.35  # Sensitivity for Left turns
    speed = 0.35
    if curve_val > 0:
        sensitivity = 0.35  # Sensitivity for Right turns
        if curve_val < 0.05:
            curve_val = 0
    else:
        if curve_val > -0.05:
            curve_val = 0

    total_curve = curve_val * sensitivity

    print(total_curve)

    Movement.direction(speed, total_curve, 0.05)

    ### For use with a working Ultrasonic Sensor ###

    # if sensor.is_too_close() == True:
    #    Usensor = 0
    #    sleep(0.1)
    # else:
    #    Usensor = 1
    #    sleep(0.1)

    # if Usensor == 1:
    #    Movement.stop

    # else:
    #    Movement.direction (speed,total_curve,0.05)


if __name__ == '__main__':
    while True:
        car_main()
