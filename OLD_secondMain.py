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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_shellMovementCamera = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_shellMovementCamera.setGeometry(QtCore.QRect(0, 0, 311, 361))
        self.tabWidget_shellMovementCamera.setObjectName("tabWidget_shellMovementCamera")
        self.tab_shellMovement = QtWidgets.QWidget()
        self.tab_shellMovement.setObjectName("tab_shellMovement")
        self.frame_shellMovement = QtWidgets.QFrame(self.tab_shellMovement)
        self.frame_shellMovement.setGeometry(QtCore.QRect(0, 0, 301, 331))
        self.frame_shellMovement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_shellMovement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_shellMovement.setObjectName("frame_shellMovement")
        self.listWidget_backgroundShellMovement = QtWidgets.QListWidget(self.frame_shellMovement)
        self.listWidget_backgroundShellMovement.setGeometry(QtCore.QRect(0, 50, 301, 291))
        self.listWidget_backgroundShellMovement.setObjectName("listWidget_backgroundShellMovement")
        self.verticalSlider_straightMovement = QtWidgets.QSlider(self.frame_shellMovement)
        self.verticalSlider_straightMovement.setGeometry(QtCore.QRect(200, 80, 51, 160))
        self.verticalSlider_straightMovement.setMinimum(-255)
        self.verticalSlider_straightMovement.setMaximum(255)
        self.verticalSlider_straightMovement.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_straightMovement.setObjectName("verticalSlider_straightMovement")
        self.plainTextEdit_straightMovementValue = QtWidgets.QPlainTextEdit(self.frame_shellMovement)
        self.plainTextEdit_straightMovementValue.setGeometry(QtCore.QRect(200, 250, 51, 21))
        self.plainTextEdit_straightMovementValue.setObjectName("plainTextEdit_straightMovementValue")
        self.horizontalSlider_pendulum = QtWidgets.QSlider(self.frame_shellMovement)
        self.horizontalSlider_pendulum.setGeometry(QtCore.QRect(10, 140, 151, 41))
        self.horizontalSlider_pendulum.setMinimum(-30)
        self.horizontalSlider_pendulum.setMaximum(30)
        self.horizontalSlider_pendulum.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pendulum.setObjectName("horizontalSlider_pendulum")
        self.plainTextEdit_pendulumValue = QtWidgets.QPlainTextEdit(self.frame_shellMovement)
        self.plainTextEdit_pendulumValue.setGeometry(QtCore.QRect(60, 190, 51, 21))
        self.plainTextEdit_pendulumValue.setObjectName("plainTextEdit_pendulumValue")
        self.textBrowser_shellMovementTitle = QtWidgets.QTextBrowser(self.frame_shellMovement)
        self.textBrowser_shellMovementTitle.setGeometry(QtCore.QRect(0, 0, 301, 31))
        self.textBrowser_shellMovementTitle.setObjectName("textBrowser_shellMovementTitle")
        self.pushButton_shellMovementSave = QtWidgets.QPushButton(self.frame_shellMovement)
        self.pushButton_shellMovementSave.setGeometry(QtCore.QRect(60, 240, 61, 31))
        self.pushButton_shellMovementSave.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"border-size: auto;\n"
"background: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(85, 170, 255,190);\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(85, 170, 255,120);\n"
"}\n"
"")
        self.pushButton_shellMovementSave.setObjectName("pushButton_shellMovementSave")
        self.tabWidget_shellMovementCamera.addTab(self.tab_shellMovement, "")
        self.tab_camera = QtWidgets.QWidget()
        self.tab_camera.setObjectName("tab_camera")
        self.frame_camera = QtWidgets.QFrame(self.tab_camera)
        self.frame_camera.setGeometry(QtCore.QRect(0, 0, 311, 341))
        self.frame_camera.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_camera.setObjectName("frame_camera")
        self.pushButton_startCamera = QtWidgets.QPushButton(self.frame_camera)
        self.pushButton_startCamera.setGeometry(QtCore.QRect(60, 10, 61, 31))
        self.pushButton_startCamera.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(0, 255, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(0, 255, 0, 90)\n"
"}\n"
"")
        self.pushButton_startCamera.setObjectName("pushButton_startCamera")
        self.pushButton_stopCamera = QtWidgets.QPushButton(self.frame_camera)
        self.pushButton_stopCamera.setGeometry(QtCore.QRect(160, 10, 61, 31))
        self.pushButton_stopCamera.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(255, 0, 0)\n"
"}\n"
"QPushButton:hover{\n"
"background: rgba(255, 0, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(255, 0, 0, 90)\n"
"}\n"
"")
        self.pushButton_stopCamera.setObjectName("pushButton_stopCamera")
        self.label_camera = QtWidgets.QLabel(self.frame_camera)
        self.label_camera.setGeometry(QtCore.QRect(0, 50, 301, 281))
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.tabWidget_shellMovementCamera.addTab(self.tab_camera, "")
        self.frame_shellOpening = QtWidgets.QFrame(self.centralwidget)
        self.frame_shellOpening.setGeometry(QtCore.QRect(0, 360, 311, 51))
        self.frame_shellOpening.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_shellOpening.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_shellOpening.setObjectName("frame_shellOpening")
        self.pushButton_shellOpen = QtWidgets.QPushButton(self.frame_shellOpening)
        self.pushButton_shellOpen.setGeometry(QtCore.QRect(70, 10, 61, 31))
        self.pushButton_shellOpen.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(0, 255, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(0, 255, 0, 90)\n"
"}\n"
"")
        self.pushButton_shellOpen.setObjectName("pushButton_shellOpen")
        self.pushButton_shellClose = QtWidgets.QPushButton(self.frame_shellOpening)
        self.pushButton_shellClose.setGeometry(QtCore.QRect(150, 10, 61, 31))
        self.pushButton_shellClose.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(255, 0, 0)\n"
"}\n"
"QPushButton:hover{\n"
"background: rgba(255, 0, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(255, 0, 0, 90)\n"
"}\n"
"")
        self.pushButton_shellClose.setObjectName("pushButton_shellClose")
        self.listWidget_backgroundShellOpening = QtWidgets.QListWidget(self.frame_shellOpening)
        self.listWidget_backgroundShellOpening.setGeometry(QtCore.QRect(-10, 0, 321, 51))
        self.listWidget_backgroundShellOpening.setObjectName("listWidget_backgroundShellOpening")
        self.listWidget_backgroundShellOpening.raise_()
        self.pushButton_shellOpen.raise_()
        self.pushButton_shellClose.raise_()
        self.frame_data = QtWidgets.QFrame(self.centralwidget)
        self.frame_data.setGeometry(QtCore.QRect(310, 10, 101, 401))
        self.frame_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_data.setObjectName("frame_data")
        self.listWidget_backgroundData = QtWidgets.QListWidget(self.frame_data)
        self.listWidget_backgroundData.setGeometry(QtCore.QRect(0, -10, 101, 411))
        self.listWidget_backgroundData.setMovement(QtWidgets.QListView.Static)
        self.listWidget_backgroundData.setObjectName("listWidget_backgroundData")
        self.pushButton_dataSend = QtWidgets.QPushButton(self.frame_data)
        self.pushButton_dataSend.setGeometry(QtCore.QRect(20, 130, 61, 31))
        self.pushButton_dataSend.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(0, 255, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(0, 255, 0, 90)\n"
"}\n"
"")
        self.pushButton_dataSend.setObjectName("pushButton_dataSend")
        self.plainTextEdit_console = QtWidgets.QPlainTextEdit(self.frame_data)
        self.plainTextEdit_console.setGeometry(QtCore.QRect(10, 170, 81, 221))
        self.plainTextEdit_console.setObjectName("plainTextEdit_console")
        self.textBrowser_sensorsDisplay = QtWidgets.QTextBrowser(self.frame_data)
        self.textBrowser_sensorsDisplay.setGeometry(QtCore.QRect(10, 10, 81, 51))
        self.textBrowser_sensorsDisplay.setStyleSheet("QTextBrowser{\n"
"background:rgb(0, 0, 0);\n"
"color:white\n"
"}")
        self.textBrowser_sensorsDisplay.setObjectName("textBrowser_sensorsDisplay")
        self.pushButton_dataRetrieve = QtWidgets.QPushButton(self.frame_data)
        self.pushButton_dataRetrieve.setGeometry(QtCore.QRect(20, 70, 61, 31))
        self.pushButton_dataRetrieve.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(255, 0, 0)\n"
"}\n"
"QPushButton:hover{\n"
"background: rgba(255, 0, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(255, 0, 0, 90)\n"
"}\n"
"")
        self.pushButton_dataRetrieve.setObjectName("pushButton_dataRetrieve")
        self.frame_statusBarLogo = QtWidgets.QFrame(self.centralwidget)
        self.frame_statusBarLogo.setGeometry(QtCore.QRect(0, 410, 671, 51))
        self.frame_statusBarLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_statusBarLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_statusBarLogo.setObjectName("frame_statusBarLogo")
        self.listWidget_backgroundStatusBar = QtWidgets.QListWidget(self.frame_statusBarLogo)
        self.listWidget_backgroundStatusBar.setGeometry(QtCore.QRect(50, 0, 621, 51))
        self.listWidget_backgroundStatusBar.setObjectName("listWidget_backgroundStatusBar")
        self.frame_logo = QtWidgets.QFrame(self.frame_statusBarLogo)
        self.frame_logo.setGeometry(QtCore.QRect(0, 0, 51, 51))
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.frame_handMovement = QtWidgets.QFrame(self.centralwidget)
        self.frame_handMovement.setGeometry(QtCore.QRect(410, 300, 271, 111))
        self.frame_handMovement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_handMovement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_handMovement.setObjectName("frame_handMovement")
        self.dial_handRotation = QtWidgets.QDial(self.frame_handMovement)
        self.dial_handRotation.setGeometry(QtCore.QRect(20, 20, 71, 61))
        self.dial_handRotation.setMaximum(359)
        self.dial_handRotation.setObjectName("dial_handRotation")
        self.pushButton_handOpen = QtWidgets.QPushButton(self.frame_handMovement)
        self.pushButton_handOpen.setGeometry(QtCore.QRect(110, 30, 61, 31))
        self.pushButton_handOpen.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(0, 255, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(0, 255, 0, 90)\n"
"}\n"
"")
        self.pushButton_handOpen.setObjectName("pushButton_handOpen")
        self.pushButton_handClose = QtWidgets.QPushButton(self.frame_handMovement)
        self.pushButton_handClose.setGeometry(QtCore.QRect(180, 30, 61, 31))
        self.pushButton_handClose.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(255, 0, 0)\n"
"}\n"
"QPushButton:hover{\n"
"background: rgba(255, 0, 0, 170)\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(255, 0, 0, 90)\n"
"}\n"
"")
        self.pushButton_handClose.setObjectName("pushButton_handClose")
        self.listWidget_backgroundHandMovement = QtWidgets.QListWidget(self.frame_handMovement)
        self.listWidget_backgroundHandMovement.setGeometry(QtCore.QRect(0, 0, 261, 111))
        self.listWidget_backgroundHandMovement.setObjectName("listWidget_backgroundHandMovement")
        self.plainTextEdit_handRotationValue = QtWidgets.QPlainTextEdit(self.frame_handMovement)
        self.plainTextEdit_handRotationValue.setGeometry(QtCore.QRect(30, 80, 51, 21))
        self.plainTextEdit_handRotationValue.setObjectName("plainTextEdit_handRotationValue")
        self.pushButton_handMovementSave = QtWidgets.QPushButton(self.frame_handMovement)
        self.pushButton_handMovementSave.setGeometry(QtCore.QRect(140, 70, 61, 31))
        self.pushButton_handMovementSave.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(85, 170, 255,190);\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(85, 170, 255,120);\n"
"}\n"
"")
        self.pushButton_handMovementSave.setObjectName("pushButton_handMovementSave")
        self.textBrowser_handMovementTitle = QtWidgets.QTextBrowser(self.frame_handMovement)
        self.textBrowser_handMovementTitle.setGeometry(QtCore.QRect(0, 0, 261, 21))
        self.textBrowser_handMovementTitle.setObjectName("textBrowser_handMovementTitle")
        self.listWidget_backgroundHandMovement.raise_()
        self.dial_handRotation.raise_()
        self.pushButton_handOpen.raise_()
        self.pushButton_handClose.raise_()
        self.plainTextEdit_handRotationValue.raise_()
        self.pushButton_handMovementSave.raise_()
        self.textBrowser_handMovementTitle.raise_()
        self.frame_armMovement = QtWidgets.QFrame(self.centralwidget)
        self.frame_armMovement.setGeometry(QtCore.QRect(410, 10, 261, 281))
        self.frame_armMovement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_armMovement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_armMovement.setObjectName("frame_armMovement")
        self.listWidget_backgroundArmMovement = QtWidgets.QListWidget(self.frame_armMovement)
        self.listWidget_backgroundArmMovement.setGeometry(QtCore.QRect(0, 0, 261, 291))
        self.listWidget_backgroundArmMovement.setObjectName("listWidget_backgroundArmMovement")
        self.dial_armShoulder = QtWidgets.QDial(self.frame_armMovement)
        self.dial_armShoulder.setGeometry(QtCore.QRect(20, 100, 81, 111))
        self.dial_armShoulder.setMaximum(180)
        self.dial_armShoulder.setObjectName("dial_armShoulder")
        self.verticalSlider_armSecondShoulder = QtWidgets.QSlider(self.frame_armMovement)
        self.verticalSlider_armSecondShoulder.setGeometry(QtCore.QRect(110, 80, 51, 160))
        self.verticalSlider_armSecondShoulder.setMinimum(-90)
        self.verticalSlider_armSecondShoulder.setMaximum(90)
        self.verticalSlider_armSecondShoulder.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_armSecondShoulder.setObjectName("verticalSlider_armSecondShoulder")
        self.verticalSlider_armElbow = QtWidgets.QSlider(self.frame_armMovement)
        self.verticalSlider_armElbow.setGeometry(QtCore.QRect(180, 80, 51, 160))
        self.verticalSlider_armElbow.setMinimum(-90)
        self.verticalSlider_armElbow.setMaximum(90)
        self.verticalSlider_armElbow.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_armElbow.setObjectName("verticalSlider_armElbow")
        self.plainTextEdit_armShoulderValue = QtWidgets.QPlainTextEdit(self.frame_armMovement)
        self.plainTextEdit_armShoulderValue.setGeometry(QtCore.QRect(30, 210, 61, 21))
        self.plainTextEdit_armShoulderValue.setObjectName("plainTextEdit_armShoulderValue")
        self.plainTextEdit_armSecondShoulderValue = QtWidgets.QPlainTextEdit(self.frame_armMovement)
        self.plainTextEdit_armSecondShoulderValue.setGeometry(QtCore.QRect(110, 250, 51, 21))
        self.plainTextEdit_armSecondShoulderValue.setObjectName("plainTextEdit_armSecondShoulderValue")
        self.plainTextEdit_armElbowValue = QtWidgets.QPlainTextEdit(self.frame_armMovement)
        self.plainTextEdit_armElbowValue.setGeometry(QtCore.QRect(180, 250, 51, 21))
        self.plainTextEdit_armElbowValue.setObjectName("plainTextEdit_armElbowValue")
        self.pushButton_armMovementSave = QtWidgets.QPushButton(self.frame_armMovement)
        self.pushButton_armMovementSave.setGeometry(QtCore.QRect(30, 240, 61, 31))
        self.pushButton_armMovementSave.setStyleSheet("QPushButton {\n"
"border-radius: 3px;\n"
"background: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background: rgba(85, 170, 255,190);\n"
"}\n"
"QPushButton:pressed{\n"
"background: rgba(85, 170, 255,120);\n"
"}\n"
"")
        self.pushButton_armMovementSave.setObjectName("pushButton_armMovementSave")
        self.textBrowser_armMovementTitle = QtWidgets.QTextBrowser(self.frame_armMovement)
        self.textBrowser_armMovementTitle.setGeometry(QtCore.QRect(0, 0, 261, 31))
        self.textBrowser_armMovementTitle.setObjectName("textBrowser_armMovementTitle")
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

        #Create the Thread for the Camera creating an object of the class Camera(QThread class)
        #Here is calling the INIT method inside the Camera Class
        self.cam = Camera.Camera(self)

        #Start() call the Run method inside the Camera class
        self.cam.start()

        #self.cam.finished.connect(self.close) #To stop the camera, it has to be implemented
        
        #Whenever you receive a Signal called updateFrame call the method setImage
        self.cam.updateFrame.connect(self.setImage)

    @Slot(QImage)
    def setImage(self, image):
        self.label_camera.setPixmap(QPixmap.fromImage(image))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_shellMovementTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Shell Movement</span></p></body></html>"))
        self.pushButton_shellMovementSave.setText(_translate("MainWindow", "Save"))
        self.tabWidget_shellMovementCamera.setTabText(self.tabWidget_shellMovementCamera.indexOf(self.tab_shellMovement), _translate("MainWindow", "Tab 1"))
        self.pushButton_startCamera.setText(_translate("MainWindow", "Start"))
        self.pushButton_stopCamera.setText(_translate("MainWindow", "Stop"))
        self.tabWidget_shellMovementCamera.setTabText(self.tabWidget_shellMovementCamera.indexOf(self.tab_camera), _translate("MainWindow", "Tab 2"))
        self.pushButton_shellOpen.setText(_translate("MainWindow", "Open"))
        self.pushButton_shellClose.setText(_translate("MainWindow", "Close"))
        self.pushButton_dataSend.setText(_translate("MainWindow", " Send Data"))
        self.plainTextEdit_console.setPlainText(_translate("MainWindow", "Modifica 1\n"
"Modifica 2\n"
"Modifica 3"))
        self.textBrowser_sensorsDisplay.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Temperature: none</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Battery: none</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed: none</p></body></html>"))
        self.pushButton_dataRetrieve.setText(_translate("MainWindow", "Retrieve Data"))
        self.pushButton_handOpen.setText(_translate("MainWindow", "Open"))
        self.pushButton_handClose.setText(_translate("MainWindow", "Close"))
        self.pushButton_handMovementSave.setText(_translate("MainWindow", "Save"))
        self.textBrowser_handMovementTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Hand movement</span></p></body></html>"))
        self.pushButton_armMovementSave.setText(_translate("MainWindow", "Save"))
        self.textBrowser_armMovementTitle.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Arm Movement</span></p></body></html>"))


app = QtWidgets.QApplication(sys.argv)
#Creating an object of the Class MaiWindow called ui
ui = Ui_MainWindow()

ui.show()

sys.exit(app.exec())
