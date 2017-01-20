import cv2
import numpy as np
import pika
import sys

#host_input_name = raw_input("Please Connect to a Host ")

credentials = pika.PlainCredentials('username', 'password')
parameters = pika.ConnectionParameters('172.20.36.177', credentials=credentials)

#Sends a message
def send(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = host_input_name))
    channel = connection.channel()
    channel.queue_declare(queue = 'dem')
    channel.basic_publish(exchange = '',  routing_key = 'dem',  body = msg)
    
#Camera
cam1 = cv2.VideoCapture(0)

#Counter
c = 0

#Main Loop
while(True):
    #Camera One Updates
    ret,  frame1 = cam1.read()
    #cam_one_raw = cv2.cvtColor(frame1,  cv2.COLOR_BGR2RGB)
    img = cv2.imencode('.png',  frame1)[1].tostring()
    send(img)
    cv2.imwrite("Sent"+str(c)+".png",  frame1)
    c += 1
    key = cv2.waitKey(20)
    #if key == 27: # exit on ESCAPE
        #connection.close()
        #break
