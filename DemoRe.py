import cv2
import pika
import numpy as np
import uuid
credentials = pika.PlainCredentials('demo', 'demo')
parameters = pika.ConnectionParameters('172.20.93.234', 5672,  '/', credentials=credentials)

class CameraRpcClient(object):
    def _init_(self):
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        result = self.channel()
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,  no_ack = True,  queue=self.callback_queue)

def on_response(self,  ch,  method,  props,  body):
    if self.corr_id == props.correlation_id:
        self.response = body

def call(self):
        self.response = None
        self.corr_id = str(uuid.uuid())
        self.channel.basic_publish(exchange = '',  routing_key = 'q1',  properties = pika.BasicProperties(reply_to = self.callback_queue,  correlation_id = self.corr_id,),  body = None)
        while self.response is None: 
            self.connection.process_data_events()
        #return self.response
        img = cv2.imdecode(self.response,  cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow('Picture', img)
        
cam_rpc = CameraRpcClient()

