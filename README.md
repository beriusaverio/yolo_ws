# yolo_ws
a ROS ws for handling the people detection through yolov3-tiny of 3 frame from 3 different camera at the same time.

## Prerequisites: 
ROS melodic
Python 2.7
USB_CAM package in your ROS ws
[Darknet](https://github.com/pjreddie/darknet) - _by pjreddie

### ROS importation in python list 
* from std_msgs.msg import Int8, String
* from sensor_msgs.msg import Image, CameraInfo
* from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
### Python importation list 
* rospy
* sys
* message_filters
* time
* os
* numpy
* ctypes
* os
* numpy
* math
* random
### install USB_CAM 
you have to install USB_CAM to satisfy its dependencies during build.
''''
sudo apt-get install ros-melodic-usb-cam
''''
