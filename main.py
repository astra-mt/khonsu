from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QSize, QObject, Signal, Slot, QEvent, QTimer

import os
import cv2
import sys
import time
import signal
import qimage2ndarray
from datetime import datetime
from Threads.Camera import Camera


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        MainWindow = self
        MainWindow.setObjectName("Ui_MainWindow")
        MainWindow.setAccessibleName("Ui_MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        

        # self.centralwidget.QsizePolicy = (QtWidgets.QSizePolicy)    
  

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")


        self.tabWidget_shellMovementCamera = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_shellMovementCamera.setObjectName("tabWidget_shellMovementCamera")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("Shell Movement")
        self.tabWidget_shellMovementCamera.addTab(self.tab, "Shell Movement")
        #Creating the label for the Camera
        self.tab_2 = QtWidgets.QLabel(MainWindow)  
        self.tab_2.setObjectName("Camera")
        #Create a tab with the Label inside
        self.tabWidget_shellMovementCamera.addTab(self.tab_2, "Camera")

        # self.listWidget_centralTab = QtWidgets.QListWidget(self.centralwidget)
        # self.listWidget_centralTab.setMovement(QtWidgets.QListView.Static)
        # self.listWidget_centralTab.setObjectName("listWidget_centralTab")


        

        # # ADD A START CAMERA BUTTON
        # self.pushButton_startCamera = QtWidgets.QPushButton(MainWindow)
        # self.pushButton_startCamera.setObjectName("pushButton_startCamera")
        # self.gridLayout.addWidget(self.pushButton_startCamera)

        # # ADD A STOP CAMERA BUTTON
        # self.pushButton_stopCamera = QtWidgets.QPushButton(MainWindow)
        # self.pushButton_stopCamera.setObjectName("pushButton_stopCamera")
        # self.gridLayout.addWidget(self.pushButton_stopCamera)


        self.gridLayout.addWidget(self.tabWidget_shellMovementCamera, 0, 0, 2, 1)
        self.listWidget_centralTab = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_centralTab.setMovement(QtWidgets.QListView.Static)
        self.listWidget_centralTab.setObjectName("listWidget_centralTab")
        self.gridLayout.addWidget(self.listWidget_centralTab, 0, 1, 3, 1)
        self.listWidget_armMovement = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_armMovement.setObjectName("listWidget_armMovement")
        self.gridLayout.addWidget(self.listWidget_armMovement, 0, 2, 1, 1)
        self.listWidget_handMovement = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_handMovement.setObjectName("listWidget_handMovement")
        self.gridLayout.addWidget(self.listWidget_handMovement, 1, 2, 2, 1)
        self.listWidget_shellOpening = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_shellOpening.setObjectName("listWidget_shellOpening")
        self.gridLayout.addWidget(self.listWidget_shellOpening, 2, 0, 1, 1)
        self.listWidget_statusBar = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_statusBar.setObjectName("listWidget_statusBar")
        self.gridLayout.addWidget(self.listWidget_statusBar, 3, 0, 1, 3)





        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)








        self.retranslateUi(MainWindow)
        self.tabWidget_shellMovementCamera.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Create the Thread for the Camera
        self.cam = Camera.Camera(self)
        #print("Camera") #Debugging
        self.cam.start()
        self.cam.finished.connect(self.close)
        self.cam.updateFrame.connect(self.setImage)







    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget_shellMovementCamera.setTabText(self.tabWidget_shellMovementCamera.indexOf(self.tab), _translate("MainWindow", "ShellMovement"))
        self.tabWidget_shellMovementCamera.setTabText(self.tabWidget_shellMovementCamera.indexOf(self.tab_2), _translate("MainWindow", "Camera"))
        # self.pushButton_startCamera.setText("Start Camera")
        # self.pushButton_stopCamera.setText("Stop Camera")





    @Slot(QImage)
    def setImage(self, image):
        #print("Prendo") #Debugging
        self.tab_2.setPixmap(QPixmap.fromImage(image))







if __name__ == "__main__":

    #print("Ciao") #Debugging
    app = QtWidgets.QApplication(sys.argv)
    
    ui = Ui_MainWindow()
    ui.show()

    sys.exit(app.exec())

