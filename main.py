from typing import Optional

import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QSize, QObject, Signal, Slot, QEvent, QTimer, SIGNAL

import os
import cv2
import sys
import time
import signal
import qimage2ndarray
from datetime import datetime
from Threads.Camera import Camera
from Threads.Sensors import Sensors
# from Threads.Sensors import Astruino

from bleak import BleakScanner, BleakClient, BleakError

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QTextBrowser,
    QToolBox, QVBoxLayout, QWidget)


SAVELOG_PATH = os.getcwd()




class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        MainWindow = self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 500)

#-------------INITIALIZE THE GUI AS A GRID LAYOUT---------------------------

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

#-------SHELL OPENING ------------------------------------------------------

        #setting a groupbox to put inside all the widgets
        self.shellOpeningGroup = QGroupBox(self.centralwidget)
        self.shellOpeningGroup.setObjectName(u"shellOpeningGroup")

        #size policies -only touch here if you know what you are doing-
        self.shellOpeningGroup.setMinimumSize(QSize(200, 0))
        self.shellOpeningGroup.setMaximumSize(QSize(16777215, 250))

        #to have a background
        self.shellOpeningGroup.setAutoFillBackground(True)                                             

        #initializing the box for the title  
        self.shellOpenClose_andTitle = QVBoxLayout(self.shellOpeningGroup)
        self.shellOpenClose_andTitle.setObjectName(u"shellOpenClose_andTitle")
        #initializing the title
        self.textBrowser_shellOpeningTitle = QTextBrowser(self.shellOpeningGroup)
        self.textBrowser_shellOpeningTitle.setObjectName(u"textBrowser_shellOpeningTitle")
        self.textBrowser_shellOpeningTitle.setMaximumSize(QSize(16777215, 50))

        #ADDING THE TITLE to the group
        self.shellOpenClose_andTitle.addWidget(self.textBrowser_shellOpeningTitle)

        self.groupBox = QGroupBox(self.shellOpeningGroup)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 60))
        self.shellOpenClose = QHBoxLayout(self.groupBox)
        self.shellOpenClose.setObjectName(u"shellOpenClose")
        self.pushButton_shellOpen = QPushButton(self.groupBox)
        self.pushButton_shellOpen.setObjectName(u"pushButton_shellOpen")
        self.pushButton_shellOpen.setMaximumSize(QSize(16777215, 50))
        self.pushButton_shellOpen.setStyleSheet(u"QPushButton {\n"
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
        #adding the shellOpen pushButton to the shellOpenClose widget
        self.shellOpenClose.addWidget(self.pushButton_shellOpen)


        #defining the shellClose pushButton
        self.pushButton_shellClose = QPushButton(self.groupBox)
        self.pushButton_shellClose.setObjectName(u"pushButton_shellClose")
        self.pushButton_shellClose.setMaximumSize(QSize(16777215, 50))
        self.pushButton_shellClose.setStyleSheet(u"QPushButton {\n"
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

        #ADDING THE shellClose pushButton TO THE shellOpenClose WIDGET
        self.shellOpenClose.addWidget(self.pushButton_shellClose)


        #ADDING THE WHOLE WIDGET TO THE GROUP
        self.shellOpenClose_andTitle.addWidget(self.groupBox)

        #SETTING THE LAYOUT
        self.gridLayout.addWidget(self.shellOpeningGroup, 1, 0, 1, 1)



#-------STATUS BAR ------------------------------------------------------

        self.statusbarGroup = QGroupBox(self.centralwidget)
        self.statusbarGroup.setObjectName(u"statusbarGroup")
        self.statusbarGroup.setMaximumSize(QSize(16777215, 100))
        self.statusbarGroup.setAutoFillBackground(True)
        self.statusBar = QHBoxLayout(self.statusbarGroup)
        self.statusBar.setObjectName(u"statusBar")
        self.frame_logo = QLabel(self.statusbarGroup)
        self.frame_logo.setObjectName(u"frame_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy)
        self.frame_logo.setMaximumSize(QSize(100, 100))
        self.frame_logo.setAutoFillBackground(True)

        self.statusBar.addWidget(self.frame_logo)

        self.textBrowser_armMovementTitle_2 = QTextBrowser(self.statusbarGroup)
        self.textBrowser_armMovementTitle_2.setObjectName(u"textBrowser_armMovementTitle_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser_armMovementTitle_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_armMovementTitle_2.setSizePolicy(sizePolicy1)
        self.textBrowser_armMovementTitle_2.setMaximumSize(QSize(16777215, 100))
        self.textBrowser_armMovementTitle_2.setAutoFillBackground(True)

        self.statusBar.addWidget(self.textBrowser_armMovementTitle_2)


        self.gridLayout.addWidget(self.statusbarGroup, 2, 0, 1, 3)


#-------SENSOR DATA AND CONSOLE (MIDDLE COLUMN) ------------------------------------------------------

        self.sensorDataGroup = QGroupBox(self.centralwidget)
        self.sensorDataGroup.setObjectName(u"sensorDataGroup")
        sizePolicy.setHeightForWidth(self.sensorDataGroup.sizePolicy().hasHeightForWidth())
        self.sensorDataGroup.setSizePolicy(sizePolicy)
        self.sensorDataGroup.setMinimumSize(QSize(150, 0))
        self.sensorDataGroup.setMaximumSize(QSize(200, 16777215))
        self.sensorDataGroup.setAutoFillBackground(True)
        self.sensorsData = QVBoxLayout(self.sensorDataGroup)
        self.sensorsData.setObjectName(u"sensorsData")

        self.textBrowser_sensorsDisplay = QTextBrowser(self.sensorDataGroup)
        self.textBrowser_sensorsDisplay.setObjectName(u"textBrowser_sensorsDisplay")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textBrowser_sensorsDisplay.sizePolicy().hasHeightForWidth())
        self.textBrowser_sensorsDisplay.setSizePolicy(sizePolicy2)
        self.textBrowser_sensorsDisplay.setMaximumSize(QSize(16777215, 60))
        self.textBrowser_sensorsDisplay.setStyleSheet(u"QTextBrowser{\n"
"background:rgb(0, 0, 0);\n"
"color:white\n"
"}")
        self.sensorsData.addWidget(self.textBrowser_sensorsDisplay)

        self.pushButton_dataRetrieve = QPushButton(self.sensorDataGroup)
        self.pushButton_dataRetrieve.setObjectName(u"pushButton_dataRetrieve")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_dataRetrieve.sizePolicy().hasHeightForWidth())
        self.pushButton_dataRetrieve.setSizePolicy(sizePolicy3)
        self.pushButton_dataRetrieve.setMaximumSize(QSize(16777215, 50))
        self.pushButton_dataRetrieve.setStyleSheet(u"QPushButton {\n"
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
        self.sensorsData.addWidget(self.pushButton_dataRetrieve)

        self.plainTextEdit_console = QPlainTextEdit(self.sensorDataGroup)
        self.plainTextEdit_console.setObjectName(u"plainTextEdit_console")
        sizePolicy2.setHeightForWidth(self.plainTextEdit_console.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_console.setSizePolicy(sizePolicy2)

        self.sensorsData.addWidget(self.plainTextEdit_console)

        self.pushButton_dataSend = QPushButton(self.sensorDataGroup)
        self.pushButton_dataSend.setObjectName(u"pushButton_dataSend")
        sizePolicy3.setHeightForWidth(self.pushButton_dataSend.sizePolicy().hasHeightForWidth())
        self.pushButton_dataSend.setSizePolicy(sizePolicy3)
        self.pushButton_dataSend.setMaximumSize(QSize(16777215, 50))
        self.pushButton_dataSend.setStyleSheet(u"QPushButton {\n"
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
        self.sensorsData.addWidget(self.pushButton_dataSend)


        self.gridLayout.addWidget(self.sensorDataGroup, 0, 1, 2, 1)

        


# STARTING THE SENSOR THREAD ---------------------------------------------

        



#-------HAND MOVEMENT ------------------------------------------------------


        self.handMovementGroup = QGroupBox(self.centralwidget)
        self.handMovementGroup.setObjectName(u"handMovementGroup")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.handMovementGroup.sizePolicy().hasHeightForWidth())
        self.handMovementGroup.setSizePolicy(sizePolicy4)
        self.handMovementGroup.setMaximumSize(QSize(16777215, 250))
        self.handMovementGroup.setAutoFillBackground(True)
        self.handMovement_andTitle = QVBoxLayout(self.handMovementGroup)
        self.handMovement_andTitle.setObjectName(u"handMovement_andTitle")
        self.textBrowser_handMovementTitle = QTextBrowser(self.handMovementGroup)
        self.textBrowser_handMovementTitle.setObjectName(u"textBrowser_handMovementTitle")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowser_handMovementTitle.sizePolicy().hasHeightForWidth())
        self.textBrowser_handMovementTitle.setSizePolicy(sizePolicy5)
        self.textBrowser_handMovementTitle.setMaximumSize(QSize(16777214, 50))
        self.textBrowser_handMovementTitle.setAutoFillBackground(True)

        self.handMovement_andTitle.addWidget(self.textBrowser_handMovementTitle)

        self.handMovementGroup_2 = QGroupBox(self.handMovementGroup)
        self.handMovementGroup_2.setObjectName(u"handMovementGroup_2")
        self.handMovementGroup_2.setAutoFillBackground(True)
        self.handMovement = QHBoxLayout(self.handMovementGroup_2)
        self.handMovement.setObjectName(u"handMovement")
        self.handRotationGroup = QGroupBox(self.handMovementGroup_2)
        self.handRotationGroup.setObjectName(u"handRotationGroup")
        sizePolicy4.setHeightForWidth(self.handRotationGroup.sizePolicy().hasHeightForWidth())
        self.handRotationGroup.setSizePolicy(sizePolicy4)
        self.handRotationGroup.setMinimumSize(QSize(60, 60))
        self.handRotationGroup.setMaximumSize(QSize(200, 16777213))
        self.handRotationGroup.setAutoFillBackground(True)
        self.handRotation = QVBoxLayout(self.handRotationGroup)
        self.handRotation.setSpacing(6)
        self.handRotation.setObjectName(u"handRotation")
        self.handRotation.setSizeConstraint(QLayout.SetMinimumSize)
        self.dial_handRotation = QDial(self.handRotationGroup)
        self.dial_handRotation.setObjectName(u"dial_handRotation")
        sizePolicy2.setHeightForWidth(self.dial_handRotation.sizePolicy().hasHeightForWidth())
        self.dial_handRotation.setSizePolicy(sizePolicy2)
        self.dial_handRotation.setMaximumSize(QSize(16777214, 300))
        self.dial_handRotation.setMaximum(359)

        self.handRotation.addWidget(self.dial_handRotation)

        self.plainTextEdit_handRotationValue = QPlainTextEdit(self.handRotationGroup)
        self.plainTextEdit_handRotationValue.setObjectName(u"plainTextEdit_handRotationValue")
        self.plainTextEdit_handRotationValue.setMaximumSize(QSize(16777213, 30))

        self.handRotation.addWidget(self.plainTextEdit_handRotationValue)


        self.handMovement.addWidget(self.handRotationGroup)

        self.hand = QGroupBox(self.handMovementGroup_2)
        self.hand.setObjectName(u"hand")
        self.hand.setMaximumSize(QSize(16777213, 16777213))
        self.hand.setAutoFillBackground(True)
        self.handGroup = QVBoxLayout(self.hand)
        self.handGroup.setObjectName(u"handGroup")
        self.handGroup.setSizeConstraint(QLayout.SetFixedSize)
        self.handGroup.setContentsMargins(-1, -1, 10, -1)
        self.handOpenCloseGroup = QGroupBox(self.hand)
        self.handOpenCloseGroup.setObjectName(u"handOpenCloseGroup")
        self.handOpenCloseGroup.setMaximumSize(QSize(16777213, 16777213))
        self.handOpenCloseGroup.setAutoFillBackground(True)
        self.handOpenClose = QHBoxLayout(self.handOpenCloseGroup)
        self.handOpenClose.setObjectName(u"handOpenClose")
        self.pushButton_handOpen = QPushButton(self.handOpenCloseGroup)
        self.pushButton_handOpen.setObjectName(u"pushButton_handOpen")
        self.pushButton_handOpen.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pushButton_handOpen.sizePolicy().hasHeightForWidth())
        self.pushButton_handOpen.setSizePolicy(sizePolicy2)
        self.pushButton_handOpen.setMaximumSize(QSize(16777213, 50))
        self.pushButton_handOpen.setAcceptDrops(True)
        self.pushButton_handOpen.setStyleSheet(u"QPushButton {\n"
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

        self.handOpenClose.addWidget(self.pushButton_handOpen)

        self.pushButton_handClose = QPushButton(self.handOpenCloseGroup)
        self.pushButton_handClose.setObjectName(u"pushButton_handClose")
        sizePolicy2.setHeightForWidth(self.pushButton_handClose.sizePolicy().hasHeightForWidth())
        self.pushButton_handClose.setSizePolicy(sizePolicy2)
        self.pushButton_handClose.setMaximumSize(QSize(16777213, 50))
        self.pushButton_handClose.setAcceptDrops(True)
        self.pushButton_handClose.setAutoFillBackground(True)
        self.pushButton_handClose.setStyleSheet(u"QPushButton {\n"
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

        self.handOpenClose.addWidget(self.pushButton_handClose)


        self.handGroup.addWidget(self.handOpenCloseGroup)

        self.pushButton_handMovementSave = QPushButton(self.hand)
        self.pushButton_handMovementSave.setObjectName(u"pushButton_handMovementSave")
        sizePolicy2.setHeightForWidth(self.pushButton_handMovementSave.sizePolicy().hasHeightForWidth())
        self.pushButton_handMovementSave.setSizePolicy(sizePolicy2)
        self.pushButton_handMovementSave.setMaximumSize(QSize(16777215, 50))
        self.pushButton_handMovementSave.setStyleSheet(u"QPushButton {\n"
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

        self.handGroup.addWidget(self.pushButton_handMovementSave)


        self.handMovement.addWidget(self.hand)

        self.hand.raise_()

        self.handMovement_andTitle.addWidget(self.handMovementGroup_2)


        self.gridLayout.addWidget(self.handMovementGroup, 1, 2, 1, 1)


#-------ARM MOVEMENT ------------------------------------------------------

        self.armMovementGroup = QGroupBox(self.centralwidget)
        self.armMovementGroup.setObjectName(u"armMovementGroup")
        sizePolicy1.setHeightForWidth(self.armMovementGroup.sizePolicy().hasHeightForWidth())
        self.armMovementGroup.setSizePolicy(sizePolicy1)
        self.armMovementGroup.setMaximumSize(QSize(16777215, 16777215))
        self.armMovementGroup.setAutoFillBackground(True)
        self.armMovement_andTitle = QVBoxLayout(self.armMovementGroup)
        self.armMovement_andTitle.setObjectName(u"armMovement_andTitle")
        self.textBrowser_armMovementTitle = QTextBrowser(self.armMovementGroup)
        self.textBrowser_armMovementTitle.setObjectName(u"textBrowser_armMovementTitle")
        self.textBrowser_armMovementTitle.setMaximumSize(QSize(16777215, 50))

        self.armMovement_andTitle.addWidget(self.textBrowser_armMovementTitle)

        self.armMovement_noTitle_2 = QGroupBox(self.armMovementGroup)
        self.armMovement_noTitle_2.setObjectName(u"armMovement_noTitle_2")
        self.armMovement_noTitle = QHBoxLayout(self.armMovement_noTitle_2)
        self.armMovement_noTitle.setObjectName(u"armMovement_noTitle")

        self.shoulderSave_2 = QGroupBox(self.armMovement_noTitle_2)
        self.shoulderSave_2.setObjectName(u"shoulderSave_2")
        self.shoulderSave_2.setMaximumSize(QSize(200, 16777215))
        self.shoulderSave_2.setAutoFillBackground(True)

        self.shoulderSave = QVBoxLayout(self.shoulderSave_2)
        self.shoulderSave.setObjectName(u"shoulderSave")

        self.shoulder = QVBoxLayout()
        self.shoulder.setObjectName(u"shoulder")

        self.dial_armShoulder = QDial(self.shoulderSave_2)
        self.dial_armShoulder.setObjectName(u"dial_armShoulder")

        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.dial_armShoulder.sizePolicy().hasHeightForWidth())

        self.dial_armShoulder.setSizePolicy(sizePolicy6)
        self.dial_armShoulder.setMinimumSize(QSize(0, 100))
        self.dial_armShoulder.setMaximum(180)

        self.shoulder.addWidget(self.dial_armShoulder)

        self.plainTextEdit_armShoulderValue = QPlainTextEdit(self.shoulderSave_2)
        self.plainTextEdit_armShoulderValue.setObjectName(u"plainTextEdit_armShoulderValue")

        sizePolicy2.setHeightForWidth(self.plainTextEdit_armShoulderValue.sizePolicy().hasHeightForWidth())

        self.plainTextEdit_armShoulderValue.setSizePolicy(sizePolicy2)
        self.plainTextEdit_armShoulderValue.setMaximumSize(QSize(16777215, 30))
        self.plainTextEdit_armShoulderValue.setAutoFillBackground(False)

        self.shoulder.addWidget(self.plainTextEdit_armShoulderValue)


        self.shoulderSave.addLayout(self.shoulder)

        self.pushButton_armMovementSave = QPushButton(self.shoulderSave_2)
        self.pushButton_armMovementSave.setObjectName(u"pushButton_armMovementSave")
        sizePolicy6.setHeightForWidth(self.pushButton_armMovementSave.sizePolicy().hasHeightForWidth())
        self.pushButton_armMovementSave.setSizePolicy(sizePolicy6)
        self.pushButton_armMovementSave.setMinimumSize(QSize(1, 50))
        self.pushButton_armMovementSave.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_armMovementSave.setStyleSheet(u"QPushButton {\n"
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

        self.shoulderSave.addWidget(self.pushButton_armMovementSave)


        self.armMovement_noTitle.addWidget(self.shoulderSave_2)

        self.secondShoulder_2 = QGroupBox(self.armMovement_noTitle_2)
        self.secondShoulder_2.setObjectName(u"secondShoulder_2")
        self.secondShoulder_2.setMaximumSize(QSize(100, 16777215))
        self.secondShoulder_2.setAutoFillBackground(True)
        self.secondShoulder = QVBoxLayout(self.secondShoulder_2)
        self.secondShoulder.setObjectName(u"secondShoulder")
        self.verticalSlider_armSecondShoulder = QSlider(self.secondShoulder_2)
        self.verticalSlider_armSecondShoulder.setObjectName(u"verticalSlider_armSecondShoulder")
        sizePolicy2.setHeightForWidth(self.verticalSlider_armSecondShoulder.sizePolicy().hasHeightForWidth())
        self.verticalSlider_armSecondShoulder.setSizePolicy(sizePolicy2)
        self.verticalSlider_armSecondShoulder.setMinimum(-90)
        self.verticalSlider_armSecondShoulder.setMaximum(90)
        self.verticalSlider_armSecondShoulder.setOrientation(Qt.Vertical)

        self.secondShoulder.addWidget(self.verticalSlider_armSecondShoulder)

        self.plainTextEdit_armSecondShoulderValue = QPlainTextEdit(self.secondShoulder_2)
        self.plainTextEdit_armSecondShoulderValue.setObjectName(u"plainTextEdit_armSecondShoulderValue")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.plainTextEdit_armSecondShoulderValue.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_armSecondShoulderValue.setSizePolicy(sizePolicy7)
        self.plainTextEdit_armSecondShoulderValue.setMaximumSize(QSize(16777215, 30))

        self.secondShoulder.addWidget(self.plainTextEdit_armSecondShoulderValue)


        self.armMovement_noTitle.addWidget(self.secondShoulder_2)

        self.elbow_2 = QGroupBox(self.armMovement_noTitle_2)
        self.elbow_2.setObjectName(u"elbow_2")
        self.elbow_2.setMaximumSize(QSize(100, 16777215))
        self.elbow_2.setAutoFillBackground(True)
        self.elbow = QVBoxLayout(self.elbow_2)
        self.elbow.setObjectName(u"elbow")
        self.verticalSlider_armElbow = QSlider(self.elbow_2)
        self.verticalSlider_armElbow.setObjectName(u"verticalSlider_armElbow")
        sizePolicy2.setHeightForWidth(self.verticalSlider_armElbow.sizePolicy().hasHeightForWidth())
        self.verticalSlider_armElbow.setSizePolicy(sizePolicy2)
        self.verticalSlider_armElbow.setMinimum(-90)
        self.verticalSlider_armElbow.setMaximum(90)
        self.verticalSlider_armElbow.setOrientation(Qt.Vertical)

        self.elbow.addWidget(self.verticalSlider_armElbow)

        self.plainTextEdit_armElbowValue = QPlainTextEdit(self.elbow_2)
        self.plainTextEdit_armElbowValue.setObjectName(u"plainTextEdit_armElbowValue")
        self.plainTextEdit_armElbowValue.setMaximumSize(QSize(16777215, 30))

        self.elbow.addWidget(self.plainTextEdit_armElbowValue)


        self.armMovement_noTitle.addWidget(self.elbow_2)


        self.armMovement_andTitle.addWidget(self.armMovement_noTitle_2)


        self.gridLayout.addWidget(self.armMovementGroup, 0, 2, 1, 1)


        self.pushButton_armMovementSave.clicked.connect(
                lambda : self.saveValue()
        )

#-------TOOLBOX SHELL MOVEMENT AND CAMERA ------------------------------------------------------        
        
        #Initializing the toolbox ---------------------------------------------------
        
        self.toolBox_shellMovementCamera = QToolBox(self.centralwidget)
        self.toolBox_shellMovementCamera.setObjectName(u"toolBox_shellMovementCamera")
        sizePolicy2.setHeightForWidth(self.toolBox_shellMovementCamera.sizePolicy().hasHeightForWidth())
        self.toolBox_shellMovementCamera.setSizePolicy(sizePolicy2)
        self.toolBox_shellMovementCamera.setMaximumSize(QSize(16777215, 99999))
        self.toolBox_shellMovementCamera.setMouseTracking(True)
        self.toolBox_shellMovementCamera.setTabletTracking(False)
        self.toolBox_shellMovementCamera.setAutoFillBackground(True)





#----------------------------------SHELL MOVEMENT------------------------------------------------------


        self.toolBox_shellMovementCameraPage1 = QWidget()
        self.toolBox_shellMovementCameraPage1.setObjectName(u"toolBox_shellMovementCameraPage1")
        self.verticalLayout = QVBoxLayout(self.toolBox_shellMovementCameraPage1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.shellMovementAndTitle = QGroupBox(self.toolBox_shellMovementCameraPage1)
        self.shellMovementAndTitle.setObjectName(u"shellMovementAndTitle")
        self.shellMovement_andTitle = QVBoxLayout(self.shellMovementAndTitle)
        self.shellMovement_andTitle.setObjectName(u"shellMovement_andTitle")
        self.textBrowser_shellMovementTitle = QTextBrowser(self.shellMovementAndTitle)
        self.textBrowser_shellMovementTitle.setObjectName(u"textBrowser_shellMovementTitle")
        self.textBrowser_shellMovementTitle.setMaximumSize(QSize(16777215, 50))

        self.shellMovement_andTitle.addWidget(self.textBrowser_shellMovementTitle)

        self.pendulumStraightMovement = QHBoxLayout()
        self.pendulumStraightMovement.setObjectName(u"pendulumStraightMovement")
        self.pendulumGroup = QGroupBox(self.shellMovementAndTitle)
        self.pendulumGroup.setObjectName(u"pendulumGroup")
        self.pendulumGroup.setCursor(QCursor(Qt.ArrowCursor))
        self.pendulum = QVBoxLayout(self.pendulumGroup)
        self.pendulum.setObjectName(u"pendulum")
        self.horizontalSlider_pendulum = QSlider(self.pendulumGroup)
        self.horizontalSlider_pendulum.setTickPosition(QSlider.TickPosition.TicksBothSides)

        self.horizontalSlider_pendulum.setObjectName(u"horizontalSlider_pendulum")
        self.horizontalSlider_pendulum.setMinimum(-30)
        self.horizontalSlider_pendulum.setMaximum(30)
        self.horizontalSlider_pendulum.setOrientation(Qt.Horizontal)

        self.pendulum.addWidget(self.horizontalSlider_pendulum)

        self.plainTextEdit_pendulumValue = QPlainTextEdit(self.pendulumGroup)
        self.plainTextEdit_pendulumValue.setObjectName(u"plainTextEdit_pendulumValue")
        sizePolicy2.setHeightForWidth(self.plainTextEdit_pendulumValue.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_pendulumValue.setSizePolicy(sizePolicy2)
        self.plainTextEdit_pendulumValue.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_pendulumValue.setMaximumSize(QSize(16777215, 30))

        self.pendulum.addWidget(self.plainTextEdit_pendulumValue)

        self.pushButton_shellMovementSave = QPushButton(self.pendulumGroup)
        self.pushButton_shellMovementSave.setObjectName(u"pushButton_shellMovementSave")
        self.pushButton_shellMovementSave.setMaximumSize(QSize(16777215, 50))
        self.pushButton_shellMovementSave.setAutoFillBackground(True)
        self.pushButton_shellMovementSave.setStyleSheet(u"QPushButton {\n"
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
        self.pushButton_shellMovementSave.setCheckable(False)

        self.pendulum.addWidget(self.pushButton_shellMovementSave)


        self.pendulumStraightMovement.addWidget(self.pendulumGroup)

        self.straightMovementGroup = QGroupBox(self.shellMovementAndTitle)
        self.straightMovementGroup.setObjectName(u"straightMovementGroup")
        self.straightMovement = QVBoxLayout(self.straightMovementGroup)
        self.straightMovement.setObjectName(u"straightMovement")
        self.verticalSlider_straightMovement = QSlider(self.straightMovementGroup)
        self.verticalSlider_straightMovement.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.verticalSlider_straightMovement.setObjectName(u"verticalSlider_straightMovement")
        sizePolicy2.setHeightForWidth(self.verticalSlider_straightMovement.sizePolicy().hasHeightForWidth())
        self.verticalSlider_straightMovement.setSizePolicy(sizePolicy2)
        self.verticalSlider_straightMovement.setMaximumSize(QSize(16777215, 16777215))
        self.verticalSlider_straightMovement.setMinimum(-255)
        self.verticalSlider_straightMovement.setMaximum(255)
        self.verticalSlider_straightMovement.setOrientation(Qt.Vertical)

        self.straightMovement.addWidget(self.verticalSlider_straightMovement)

        self.plainTextEdit_straightMovementValue = QPlainTextEdit(self.straightMovementGroup)
        self.plainTextEdit_straightMovementValue.setObjectName(u"plainTextEdit_straightMovementValue")
        self.plainTextEdit_straightMovementValue.setMaximumSize(QSize(16777215, 30))

        self.straightMovement.addWidget(self.plainTextEdit_straightMovementValue)


        self.pendulumStraightMovement.addWidget(self.straightMovementGroup)


        self.shellMovement_andTitle.addLayout(self.pendulumStraightMovement)


        self.verticalLayout.addWidget(self.shellMovementAndTitle)

        self.toolBox_shellMovementCamera.addItem(self.toolBox_shellMovementCameraPage1, u"Shell Movement")

        self.gridLayout.addWidget(self.toolBox_shellMovementCamera, 0, 0, 1, 1)


#--------------------------------------CAMERA------------------------------------------------------------


        #Initializing camera label and widget-----------------------------

        self.toolBox_shellMovementCameraPage2 = QWidget()
        self.toolBox_shellMovementCameraPage2.setObjectName(u"toolBox_shellMovementCameraPage2")
        sizePolicy8 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.toolBox_shellMovementCameraPage2.sizePolicy().hasHeightForWidth())
        self.toolBox_shellMovementCameraPage2.setSizePolicy(sizePolicy8)
        self.horizontalLayout = QHBoxLayout(self.toolBox_shellMovementCameraPage2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.camera_2 = QGroupBox(self.toolBox_shellMovementCameraPage2)
        self.camera_2.setObjectName(u"camera_2")
        self.camera = QVBoxLayout(self.camera_2)
        self.camera.setObjectName(u"camera")
        self.camera.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_camera = QLabel(self.camera_2)
        self.label_camera.setObjectName(u"label_camera")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_camera.sizePolicy().hasHeightForWidth())
        self.label_camera.setSizePolicy(sizePolicy9)
        self.label_camera.setMaximumSize(QSize(16777214, 16777214))

        self.camera.addWidget(self.label_camera)



        #-------------------------INITIALIZING THE CAMERA -------------------------------------
        self.cameraStartStop_2 = QGroupBox(self.camera_2)
        self.cameraStartStop_2.setObjectName(u"cameraStartStop_2")
        self.cameraStartStop_2.setMaximumSize(QSize(16777215, 60))
        self.cameraStartStop = QHBoxLayout(self.cameraStartStop_2)
        self.cameraStartStop.setSpacing(6)
        self.cameraStartStop.setObjectName(u"cameraStartStop")
        self.cameraStartStop.setContentsMargins(-1, 1, -1, -1)
        self.pushButton_startCamera = QPushButton(self.cameraStartStop_2)
        self.pushButton_startCamera.setObjectName(u"pushButton_startCamera")
        self.pushButton_startCamera.setMaximumSize(QSize(16777215, 50))
        self.pushButton_startCamera.setStyleSheet(u"QPushButton {\n"
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

        self.cameraStartStop.addWidget(self.pushButton_startCamera)

        self.pushButton_stopCamera = QPushButton(self.cameraStartStop_2)
        self.pushButton_stopCamera.setObjectName(u"pushButton_stopCamera")
        self.pushButton_stopCamera.setMaximumSize(QSize(16777215, 50))
        self.pushButton_stopCamera.setStyleSheet(u"QPushButton {\n"
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

        self.cameraStartStop.addWidget(self.pushButton_stopCamera)


        self.camera.addWidget(self.cameraStartStop_2)


        self.horizontalLayout.addWidget(self.camera_2)

        self.toolBox_shellMovementCamera.addItem(self.toolBox_shellMovementCameraPage2, u"")

        self.pushButton_dataSend.clicked.connect(
                lambda : self.astruinoCommunication()
        )

        self.dial_armShoulder.valueChanged.connect(
                lambda : self.shoulderMergeValues()
        )

#------------------ STARTING THE THREADS -----------------------------------------

        self.astro = None
        #Create the Thread for the Camera creating an object of the class Camera(QThread class)
        #Here is calling the INIT method inside the Camera Class
        self.cam = Camera.Camera(self)
        #Start() call the Run method inside the Camera class
        self.cam.start()

        #self.cam.finished.connect(self.close) #To stop the camera, it has to be implemented
        
        #Whenever you receive a Signal called updateFrame call the method setImage
        self.cam.updateFrame.connect(self.setImage)



# Setting things (i think in the toolbox)----------------------------------------------------------



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

#-- CAMERA THREAD ----------------------------------------------------------------------------------------------

    @Slot(QImage)
    def setImage(self, image):
        self.label_camera.setPixmap(QPixmap.fromImage(image))


         

#-- SENSORS THREAD ----------------------------------------------------------------------------------------------
    # starting the new thread when the button "pushButton_dataSend" is clicked, we take the string from the console
    # and we send it to the astruino
    def astruinoCommunication(self):
        value = self.plainTextEdit_console.toPlainText()
        self.plainTextEdit_console.clear()
        self.astro = Sensors.Astruino(value, self)
        self.astro.start()

    def shoulderMergeValues(self):
        self.plainTextEdit_armShoulderValue.setPlainText(str(self.dial_armShoulder.value()))

        try:
            value = int(self.plainTextEdit_armShoulderValue.toPlainText())
            self.dial_armShoulder.setValue(value)
        except ValueError:
             print("Invalid value entered. Please enter a valid integer.")

             

    def saveValue(self):
        arm_movement = self.dial_armShoulder.value()
        # hand_movement = self.pushButton_handMovementSave.text()
        # shell_movement = self.pushButton_shellMovementSave.text()  # Added parentheses here

        self.plainTextEdit_console.appendPlainText(f"{arm_movement}") # :\n {hand_movement} :\n {shell_movement}")


#----------------TRANSLATION--------------------------------------------------------------------------
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser_shellOpeningTitle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Shell Opening</span></p></body></html>", None))
        self.pushButton_shellOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_shellClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.textBrowser_armMovementTitle_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_sensorsDisplay.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Temperature: none</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Battery: none</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Speed: none</span></p></body></html>", None))
        self.pushButton_dataRetrieve.setText(QCoreApplication.translate("MainWindow", u"Retrieve Data", None))
        self.pushButton_dataSend.setText(QCoreApplication.translate("MainWindow", u" Send Data", None))
        self.textBrowser_handMovementTitle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Hand movement</span></p></body></html>", None))
        self.pushButton_handOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_handClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_handMovementSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.textBrowser_armMovementTitle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Arm Movement</span></p></body></html>", None))
        self.pushButton_armMovementSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_camera.setText("")
        self.pushButton_startCamera.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_stopCamera.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.toolBox_shellMovementCamera.setItemText(self.toolBox_shellMovementCamera.indexOf(self.toolBox_shellMovementCameraPage2), "Rover Cam")
        self.textBrowser_shellMovementTitle.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Shell Movement</span></p></body></html>", None))
        self.pushButton_shellMovementSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.toolBox_shellMovementCamera.setItemText(self.toolBox_shellMovementCamera.indexOf(self.toolBox_shellMovementCameraPage1), "Shell Movement")
    # retranslateUi





if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        #Creating an object of the Class MaiWindow called ui
        ui = Ui_MainWindow()
        ui.show()
        



        sys.exit(app.exec())
