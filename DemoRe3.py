import cv2
import pika
import numpy as np
host_in = raw_input("Plese Enter the Host: ")
connection = pika.BlockingConnection(pika.ConnectionParameters(host = host_in))
channel = connection.channel()
channel.queue_declare(queue = 'dem')

def callback(ch,  method,  properties, body):
    print(type(body)) 
    #final_name = ''.join([name, str(count), ".png"])
    nparr = np.fromstring(body,  np.uint8)
    img = cv2.imdecode(nparr,  cv2.CV_LOAD_IMAGE_COLOR)
    im = cv2.cvtColor(img,  cv2.COLOR_BGR2RGB)
    #cv2.imwrite(final_name,  im)
    cv2.imshow('Its Picture Time', im)
    
#consume
#channel.basic_consume(callback,  queue = 'cam',  no_ack = True)
#channel.start_consuming()

#Count
d = 0

#Main Loop
while(True):
    method_frame,  header_frame,  body = channel.basic_get(queue = 'dem')
    nparr = np.fromstring(body,  np.uint8)
    img = cv2.imdecode(nparr,  cv2.CV_LOAD_IMAGE_COLOR)
    im = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Received"+str(d)+".png",  im)
    d += 1
    #cv2.imshow('Its Picture Time', im)
