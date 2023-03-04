import cv2
from picamera import PiCamera
from time import sleep

cap = cv2.VideoCapture(0)


def get_vid(display=False, size=[640, 480]):
    _, img = cap.read()
    img = cv2.resize(img, (size[0], size[1]))
    if display:
        cv2.imshow('VID', img)
        cv2.waitKey(1)
    return img


def record(time=5):
    camera = PiCamera()
    camera.resolution = (640, 480)

    camera.start_preview()
    sleep(5)
    print("Recording Started")
    camera.start_recording('/home/pi/Desktop/vidNewHeight2.h264')
    sleep(time)
    print("Recording Finished")
    camera.stop_recording()
    camera.stop_preview()


if __name__ == '__main__':
    while True:
        get_vid(True)

    # record(5)
