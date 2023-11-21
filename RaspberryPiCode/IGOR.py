import serial   #Confusingly, the package for this is pySerial not serial
import time
import sys
import paramiko
import urllib
import cv2 as cv
# from cv_cmds import take_picture, crop_quadrant, get_centroid, get_contours, extract_HSV_channels
import numpy as np
import signal
import math
import io
from picamera import PiCamera


ser = serial.Serial('/dev/ttyACM1', 115200)
ser.write(b'G28 X0\r\n')

ser.close()


def camera_test():
    camera = PiCamera()
    camera.capture('/home/pi/Desktop/image.jpg')


# raspistill -o Desktop/image.jpg
# libcamera-still -o test.jpg
# scp pi@raspberrypi:test.jpg .