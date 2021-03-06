#Simple example Robot Raconteur Sawyer Robot and Cognex client
#pick up and drop detected objects
from RobotRaconteur.Client import *

import numpy as np
import time,traceback,sys
from autodiscovery import autodiscover

####################Start Service and robot setup
#auto discovery
time.sleep(2)
url=autodiscover("edu.robotraconteur.objectrecognition.ObjectRecognitionSensor","cognex")
if url==None:
	print("service not found")
	sys.exit(1)

object_recognition_sensor_data =None
def new_frame(pipe_ep):
    global object_recognition_sensor_data 

    #Loop to get the newest frame
    while (pipe_ep.Available > 0):
        #Receive the packet
        object_recognition_sensor_data =pipe_ep.ReceivePacket()

        for recognized_object in object_recognition_sensor_data.recognized_objects.recognized_objects:
        	print(recognized_object.recognized_object.name)
        	print(recognized_object.pose.pose.pose)


#Startup, connect, and pull out the camera from the objref    
c=RRN.ConnectService(url)

#Connect the pipe FrameStream to get the PipeEndpoint p
p=c.object_recognition_sensor_data.Connect(-1)
p.PacketReceivedEvent+=new_frame

input("press enter to quit")