# yolo_ws
a ROS ws for handling the people detection through yolov3-tiny of 3 frame from 3 different camera at the same time.

## Prerequisites: 
* ROS melodic
* Python 2.7
* a working CUDA in your device
* install USB_CAM to satisfy dependencies
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
download somewhere yolov3-tiny.weights.
it's a 35MB weights file you can find easily in web.
## ADAPT ws files to your path

### modify coco.data 
in line 5: 
```
names = YOUR_ABSOLUTE_PATH_TO_DARKNET_DIRECTORY/data/coco.names
```
### modify webcam.py
in line 56: 
```
lib = CDLL("YOUR_ABSOLUTE_PATH_TO_DARKNET_DIRECTORY/libdarknet.so", RTLD_GLOBAL)
```
in line 186 and 187: 
```  
net = load_net(b"YOUR_ABSOLUTE_PATH_TO_yolov3-tiny.cfg_DIRECTORY/yolov3-tiny.cfg", b"YOUR_ABSOLUTE_PATH_TO_yolov3-tiny.weights_DIRECTORY/yolov3-tiny.weights", 0)
    meta = load_meta(b"YOUR_ABSOLUTE_PATH_TO_yolo_ws_DIRECTORY/coco.data")
```
## BUILD yolo_ws
```  
cd yolo_ws
catkin_make
```
## RUN yolo_ws
make sure you have 3 working usb cameras plugged in your device and then
* in terminal 1 launch:
```  
roslaunch usb_cam usb_cam-test.launch
```
* in terminal 2 run:
```  
rosrun usb_cam usb_cam_pubber
```
* in terminal 3 call:
```  
rosservice call /usb_cam/start True
```
* in terminal 4 run

```  
rosrun people_detection webcam.py 
```
## Check detections
point a camera to a person and see if 


```  
rostopic echo /people_detection 
```
returns you a 

```  
data: "people detected"
```
