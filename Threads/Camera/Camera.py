#HERE IS A CAMERA FILE TO HANDLE THE VIDEOCAPTURE OF THE CAMERA AND DISPLAYING IT INTO THE APPROPRIATE WINDOW


import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QAction, QImage, QKeySequence, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)



class Camera(QThread):
    updateFrame = Signal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True
        self.cap = True

    def run(self):
        #Select the camera
        self.cap = cv2.VideoCapture(0)
        while True:
            #Read the frame from the Buffer
            ret, frame = self.cap.read()
            #print("Step1")#Debugging
            #cv2.imshow("Window",frame)
            #cv2.waitKey(1)
            if not ret:
                continue   
            
            #Take the Gray Gradients
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #Take the colors 
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #Scale the image to the 
            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(640, 480, Qt.KeepAspectRatio)
            #print("Step2") #Debugging

            self.updateFrame.emit(img)
            #print("Bro") #Debugging
    #sys.exit(-1)
#cam=Camera()
#cam.run()
