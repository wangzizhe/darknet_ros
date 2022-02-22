# Introduction

This implementation realizes YOLO in ROS for object detection.

**Autor:** Zizhe Wang

**Email:** zizhe.wang@tu-dresden.de

**Environment:** Ubuntu 18.04 + ROS melodic

---

To use YOLO in ROS. We need a ROS package which is able to use YOLO. For this purpose the ROS package based on YOLOv3 was used in this implementation. 

More details: 

- GitHub: [leggedrobotics/darknet_ros: YOLO ROS: Real-Time Object Detection for ROS](https://github.com/leggedrobotics/darknet_ros)
- Ros Wiki: [darknet_ros - ROS Wiki](http://wiki.ros.org/darknet_ros)

This `darknet_ros` package can be modified in order to use other versions of YOLO e.g. YOLOv4, YOLOv5. Due to time limitation only original `darknet_ros` package is included in this work.

---

Relevant Resources:

- YOLOv4, v3, v2 for Windows and Linux:

  [AlexeyAB/darknet: YOLOv4 / Scaled-YOLOv4 / YOLO - Neural Networks for Object Detection (Windows and Linux version of Darknet ) (github.com)](https://github.com/AlexeyAB/darknet)

- YOLOv5:

  [ultralytics/yolov5: YOLOv5 🚀 in PyTorch > ONNX > CoreML > TFLite (github.com)](https://github.com/ultralytics/yolov5)

**<u>! IMPORTANT TO KNOW !</u>**

YOLOv5 is **NOT** the updated version of YOLOv4! 

They are basically two different updated versions of YOLOv3 which were both proposed in middle 2020!

Each has its own characteristics!

So it is important to know which kind of characteristics suit your need then choose the proper model!

# Instructions

## File structure

```
├───catkin_ws
   ├───src
      ├───darknet_ros
      └───yolo_detection
             └───launch
```

The ROS package `darknet_ros` was cloned from the GitHub page under the `./catkin_ws/src` folder.

There is another folder under `./catkin_ws/src`  which is called `yolo_detection`. Inside this folder we can make customization depends on the tasks we have.

Inside the folder `yolo_detection` this is the folder `launch` and inside this folder a `.launch` file was created. More details of this `.launch` file are described in the file.

## How to use

1. If something changed in the `.launch` file. Run the following codes:

   - `cd catkin_ws`

   - `source devel/setup.bash`
2. Then, run the `.launch` file with the following code:
   - `roslaunch yolo_detection yolo_v3.launch`
3. The YOLO Network (e.g. for YOLOv3 there are 106 layers) will be loaded, then "*waiting for image*" will be displayed. 
4. Next, run the `.bag` file with the following code:
   - `rosbag play -l xxx.bag`
5. Finally, the result will be shown as this: https://youtu.be/hBNopumbdFI
