
import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot, QSize
from PySide6.QtGui import QAction, QImage, QKeySequence, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)
 #Creating a QThread Class for the camera, a thread is a sub-process processed meanwhile to the "main" process
class Camera(QThread):
    #To let the Threads communicate with other Threads or with the main we need to send Signal, here we create the signal
    updateFrame = Signal(QImage)
    #This is the constructor of the Class, when we create a new object of Camera class we call INIT method
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.trained_file = None
        self.status = True
        self.cap = True

    def run(self):
        #Select the camera
        self.cap = cv2.VideoCapture(0)
        #self.cap.set(cv2.CAP_PROP_BUFFERSIZE,10)   #This is to set the size of the buffer, standard is 10
        while True:
            #Read the frame from the Buffer
            ret, frame = self.cap.read()  
            
            #Check if there is a frame
            if not ret:
                continue   
            
            #Take the Gray Gradients in the frame
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #Take the colors in the frame
            color_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #Take all the size of the framwe
            h, w, ch = color_frame.shape
            img = QImage(color_frame.data, w, h, ch * w, QImage.Format_RGB888)
            scaled_img = img.scaled(301, 281, Qt.AspectRatioMode(1))
            #Emitting the Signal we created before with inside the frame
            self.updateFrame.emit(scaled_img)
        #sys.exit(-1)