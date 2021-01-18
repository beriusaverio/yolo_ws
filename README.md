# yolo_ws
a ROS ws for handling the people detection through yolov3-tiny of 3 frame from 3 different camera at the same time.

## Prerequisites: 
* ROS melodic
* Python 2.7
* a working CUDA in your device
* USB_CAM package in your ROS ws
* [Darknet](https://github.com/pjreddie/darknet) - by pjreddie

### ROS importation in python list 
* from std_msgs.msg import Int8, String
* from sensor_msgs.msg import Image, CameraInfo
* from std_srvs.srv import SetBool, SetBoolRequest, SetBoolResponse
### Python libraries importation list 
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

### modify your .bashrc to use CUDA
add:
```
export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

```
adapt it with your CUDA version. 10.2 is used in the example.

### install USB_CAM 
you have to install USB_CAM to satisfy its dependencies during build.

```
sudo apt-get install ros-melodic-usb-cam
```
### install darknet 
```
git clone https://github.com/pjreddie/darknet.git
```
change GPU=1 in the Makefile and then
```
cd Darknet
make
```
