import cv2
import numpy as np
import pika
import sys
credentials = pika.PlainCredentials('demo', 'demo')
parameters = pika.ConnectionParameters('172.20.93.234',  5672, '/', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = 'q1')

#Camera
cam1 = cv2.VideoCapture(0)

#Sends a message
def  on_request(ch,  method, props,  body):
    #Camera One Updates
    ret,  frame1 = cam1.read()
    img = cv2.imencode('.png',  frame1)[1].tostring()
    ch.basic_publish(exchange = '',  routing_key = props.reply_to,  properties = pika.BasicProperties(correlation_id = \
                                                                                                                                                                                            props.correlation_id),  body = img)
    ch.basic_ack(delivery_tag = method.delivery_tag)
    channel.basic_qos(prefetch_count = 1)
    channel.basic_consume(on_request,  queue = 'q1')
    
channel.start_consuming()
