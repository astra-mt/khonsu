from Camera import Camera
import os
import sys
import time

import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QAction, QImage, QKeySequence, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Buttons(QImage):
    
    def handle_pushButton_startCamera(self):
        self.cam = Camera(self)
        #print("Camera") #Debugging
        self.cam.start()
        self.cam.updateFrame.connect(self.setImage)

    def handle_pushButton_stopCamera(self):
        self.sys.exit(-1)

