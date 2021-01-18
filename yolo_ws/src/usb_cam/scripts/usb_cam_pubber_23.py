#!/usr/bin/env python
import rospy
import sys
import message_filters
import time
import os
from std_msgs.msg import Int8, String
from sensor_msgs.msg import Image, CameraInfo
from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
import numpy as np

class repubber():

    #def callback_1(self, img1):
     #   self.t_start1 = time.time()

    def callback_2(self, img2):
        self.t_start2 = time.time()
        

    def callback_3(self, img3):
        self.t_start3 = time.time()

    def __init__(self):
        self.start_adv = rospy.Service('/usb_cam/start', SetBool, self.start)
        self.stop_adv = rospy.Service('/usb_cam/stop', SetBool, self.stop)
        self.repubber = True
        self.black = np.zeros((480,640, 3), dtype = "uint8")
        self.pub = rospy.Publisher('/usb_cam/data', Image, queue_size=10)
        #self.pub_issue = rospy.Publisher('/usb_cam/USB_camera_issue', int8, queue_size=10)  
        self.t_start = time.time()
        self.t_start2 = time.time()
        self.t_start3 = time.time()
        self.time_th = 3
        #self.image1= np.empty([480,640,3], dtype=np.uint8)
        self.image2= np.empty([480,640,3], dtype=np.uint8)
        self.image3= np.empty([480,640,3], dtype=np.uint8)

    def callback(self, b,c):
        if self.repubber:

            #self.image1 = np.ndarray(shape=(a.height, a.width, 3),
             #                  dtype=np.uint8, buffer=a.data)

            self.image2 = np.ndarray(shape=(b.height, b.width, 3),
                               dtype=np.uint8, buffer=b.data)

            self.image3 = np.ndarray(shape=(c.height, c.width, 3),
                              dtype=np.uint8, buffer=c.data)

            #frame1 = np.array(self.image1, dtype=np.uint8)
            frame2 = np.array(self.image2, dtype=np.uint8)
            frame3 = np.array(self.image3, dtype=np.uint8)
            con = np.concatenate((frame2, frame3), axis=1)
            con2 = np.concatenate((self.black, self.black), axis=1)
            con3 = np.concatenate((con, con2), axis=0)

            img_msg = Image()
            img_msg.height = con3.shape[0]
            img_msg.width = con3.shape[1]
            img_msg.encoding= 'rgb8'
            img_msg.data = con3.tostring()
            img_msg.step = len(img_msg.data) // img_msg.height
            print("publishing with pubber23")
            self.pub.publish(img_msg)
            self.t_start = time.time()
            self.t_start2 = time.time()
            self.t_start3 = time.time()



    def start(self, req):
        if req.data:
            self.repubber = True
            return SetBoolResponse(True,'Start')
        else:
            return SetBoolResponse(True,'Ok')
    def stop(self, req):
        if req.data:
            self.repubber = False
            return SetBoolResponse(True,'Stop')
        else:
            return SetBoolResponse(True,'Ok')

    def listener(self):
        
        #image1_sub = message_filters.Subscriber("/usb_cam/image_raw", Image)
        image2_sub = message_filters.Subscriber("/usb_cam2/image_raw", Image)
        image3_sub = message_filters.Subscriber("/usb_cam3/image_raw", Image)
          
        ts = message_filters.ApproximateTimeSynchronizer([image2_sub,image3_sub],10,0.1)
        ts.registerCallback(self.callback)
   
    def main(self):
        self.listener()
        while not rospy.is_shutdown():
            rostime_now = time.time()
            #self.pub_issue.publish(1) 
            if (rostime_now-self.t_start)>self.time_th:
                #self.image2_check_sub = rospy.Subscriber("/usb_cam2/image_raw", String, self.callback_2)
                #self.image3_check_sub = rospy.Subscriber("/usb_cam3/image_raw", String, self.callback_3)
                #if (rostime_now-self.t_start2)>self.time_th:
                    #print("rotta pure la 2!")
                   # self.pub_issue.publish(2) 
                #if (rostime_now-self.t_start3)>self.time_th:
                    #self.pub_issue.publish(3)
                 #
                print("another camera broke")     


            time.sleep(2)
            rate.sleep()

if __name__ == "__main__":
    rospy.init_node('usb_cam_pub_23', anonymous=False, disable_signals=True)
    rate = rospy.Rate(10)
    try:
        t = repubber()
        t.main()
    except rospy.ROSInterruptException: pass
    rospy.spin()
    rate.sleep()

