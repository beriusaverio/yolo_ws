#!/usr/bin/env python

######## People Detection Using Tensorflow Classifier #########
#
# Author: Paolo Codignopni
# Date: 05/12/20
# Description: 
# This program uses a TensorFlow classifier to perform people detection.
# It loads the classifier uses it to perform people detection on a set of cameras.
# It draws boxes and scores around the objects of interest in each frame.

## Online reference
## https://github.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pinb

# Import packages

import numpy as np
import rospy
from darknet_ros_msgs.msg import *
from std_msgs.msg import *
from sensor_msgs.msg import *


class detec():

    def __init__(self):      
        
        # people detection topic publisher
        self.detection_pub = rospy.Publisher('/people_detection', Bool, queue_size=10)
        self.counter=0
        self.counter_th = rospy.get_param('timer')
        self.main()
    # callback for darknet_ros topic subscriber
    def callback(self, msg):
        print(".......... publishing in /people_detection")
        if msg.count > 0:
            
            self.counter = self.counter + 1
            if self.counter > self.counter_th:
                self.publish_detection( True)
            else:
                self.publish_detection( False)
        else:
            self.counter = 0
            self.publish_detection( False)   

    
    # function for publishing peopleDetection rosmessage
    def publish_detection(self, detection):

        self.detection_pub.publish(detection)         

    # main function
    def main(self):       

        rospy.Subscriber('/darknet_ros/found_object', ObjectCount, self.callback, queue_size=None)


if __name__ == "__main__":
    rospy.init_node('peopleDetTensorflow', anonymous=False, disable_signals=True)
    rate = rospy.Rate(10)
    detec()
    rospy.spin()
    rate.sleep()
