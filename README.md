# self-driving-car
Using a RaspberryPi, GoPiGo3, Python and OpenCV to create a self-driving car which follows a white path.

-------------------------------------------------------------------------------------------------

### Raspberry Pi Self-driving Car Setup Guide
------------------------------------------------
#### Libraries Needed
OpenCV 4: https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/

Numpy: Type in linux terminal: sudo pip3 install numpy

PyPs4: https://pypi.org/project/pyps4/

GoPiGo3 Libraries: https://www.dexterindustries.com/GoPiGo/get-started-with-the-gopigo3-raspberry-pi-robot/3-program-your-raspberry-pi-robot/python-programming-language/

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#### Instructions
1) Take a recording of the track you intend to use the car on by using the PlayStation module and Webcam to record the track. 

2) Import the video of the track into the colour_picker script and select the correct HSV values so the lane is correctly distinguished from the rest of the image. 

3) Place the car at the start of the track and run car_main, for any inaccuracies adjust the sensitivity in the car_main module accordingly.
