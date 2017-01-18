import cv2
import numpy as np
import pika
import sys

#Initialize Capture Devices
cam1 = cv2.VideoCapture(0)

#Ask for host name in terminal 
host_input_name = raw_input("Please Connect to a Host ")

#Connect to client
connection = pika.BlockingConnection(pika.ConnectionParameters(host = host_input_name))

channel = connection.channel()

#change the exchange name
channel.exchange_declare(exchange = 'camera_frames',  type = 'topic')

routing_key = 'camera.driver'

#Temporary RGB conversion function
#does this give delayed access to frame
#doesnt read first frame?
#def getCam1():
   # _,  frame1 = cam1.read()
    #frame1f = cv2.cvtColor(frame1,  cv2.COLOR_BGR2RGB)
    #return frame1f

#PseudoLock
#ok_to_start = raw_input("Enter password to Proceed: ")   

#Main Loop
while(True):
    #Camera One Updates
    _,  frame1 = cam1.read()
    #Does not directly use Mat so that may be why it shows blue
    camera_one_raw = cv2.cvtColor(frame1,  cv2.COLOR_BGR2RGB)
    #Gets 'dimensions' of the array
    temp = frame1.shape
    h, w = temp
    conv_frame = cv2.CreateMat(h,  w,  cv2.CV_32FC3)
    temp_frame = cv2.fromArray(frame1)
    cv2. CvtColor(temp_frame,  conv_frame,  cv2.CV_BGR2GRAY)
    #buffer = camera_one_update.tostring()
    #cv2.imshow("ASDF",  camera_one_update)
    cv2.imshow("as", conv_frame )
    #channel.basic_publish(exchange = 'camera_frames',  routing_key = routing_key,  body = )    
    key = cv2.waitKey(20)
    if key == 27: # exit on ESCAPE
        break
