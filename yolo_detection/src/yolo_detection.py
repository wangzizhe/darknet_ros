#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from sensor_msgs.msg import CameraInfo, Image
import rospy
import argparse
import cv2
from cv_bridge import CvBridge
from scipy import ndimage
import numpy as np


class Yolo_Common(object):
    def __init__(self, subscriber_topic=None, rotation_angle=None, calibration_file_path=None, frame_id=None):

        if subscriber_topic == None:
            exit("Specify subscriber topic")
        self.sub = rospy.Subscriber(subscriber_topic, Image, self.callback)
        self.subscriber_name = subscriber_topic

        publisher_name = '{}_yolo'.format(subscriber_topic)
        self.pub = rospy.Publisher(publisher_name, Image, queue_size=10)
        self.bridge = CvBridge()
        self.frame_id = frame_id

    def publish(self, data):
        self.pub.publish(data)

    def callback(self, image_date):
        rospy.loginfo_once('received image')

        cv_img = self.bridge.imgmsg_to_cv2(image_date, desired_encoding="bgr8")
        # place code here to detect objects ...yolo

        print("received image")

        # convert to ros message
        imageData = self.bridge.cv2_to_imgmsg(cv_img)
        imageData.header.frame_id = "camera"
        # publish image data
        self.publish(data=imageData)


#  ************ Main Function Call **************************************************************
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Modify Image")
    parser.add_argument("-t", "--image_topic", type=str, help="Image topic.")
    parser.add_argument("-f", "--frame_id", type=str,
                        default="camera", help="Set Frame ID ")
    args = parser.parse_args()

    rospy.init_node('yolo_image_detector', log_level=rospy.DEBUG)

    imageModifier = Yolo_Common(args.image_topic, frame_id=args.frame_id)

    sub = rospy.Subscriber(args.image_topic, Image,
                           callback=imageModifier.callback)

    rospy.spin()
    while not rospy.is_shutdown():
        pass
