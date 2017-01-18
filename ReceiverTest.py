import cv2
import numpy as np
import pika
import sys

#Test to see if rabbitmq works
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

channel.exchange_declare(exchange = 'camera_frames',  type = 'topic')

result = channel.queue_declare(exclusive = False)
queue_name = result.method.queue

def callback(ch,  method,  properties, body):
    frame = 
    cv2.imshow('Its Picture Time',  frame)
    print("asd")

while(True):
    channel.basic_consume(callback,  queue = queue_name,  no_ack = True)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESCAPE
        break
