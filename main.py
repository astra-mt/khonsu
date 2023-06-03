from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from ui.arm import ArmView
from ui.movement import MovementView
from bluetooth.astruino_ble import astruino

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(101, 101))
        self.label_3.setMaximumSize(QtCore.QSize(101, 101))
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setPixmap(QtGui.QPixmap(".\\ui\\../res/images/astra_logo-no_bg.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(-1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(21)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_home = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_home.sizePolicy().hasHeightForWidth())
        self.pushButton_home.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setStyleSheet("margin: 0rem;")
        self.pushButton_home.setObjectName("pushButton_home")
        self.verticalLayout_3.addWidget(self.pushButton_home)
        self.pushButton_movement = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_movement.sizePolicy().hasHeightForWidth())
        self.pushButton_movement.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_movement.setFont(font)
        self.pushButton_movement.setStyleSheet("margin: 0rem;")
        self.pushButton_movement.setObjectName("pushButton_movement")
        self.verticalLayout_3.addWidget(self.pushButton_movement)
        self.pushButton_arm = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_arm.sizePolicy().hasHeightForWidth())
        self.pushButton_arm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_arm.setFont(font)
        self.pushButton_arm.setStyleSheet("margin: 0rem;")
        self.pushButton_arm.setObjectName("pushButton_arm")
        self.verticalLayout_3.addWidget(self.pushButton_arm)
        self.pushButton_settings = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_settings.sizePolicy().hasHeightForWidth())
        self.pushButton_settings.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_settings.setFont(font)
        self.pushButton_settings.setStyleSheet("margin: 0rem;")
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.verticalLayout_3.addWidget(self.pushButton_settings)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.horizontalLayout.addWidget(self.frame)
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.mdiArea.cascadeSubWindows()
        self.horizontalLayout.addWidget(self.mdiArea)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.progressBar = QtWidgets.QProgressBar(self.frame_5)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.pushButton_savelog = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_savelog.sizePolicy().hasHeightForWidth())
        self.pushButton_savelog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_savelog.setFont(font)
        self.pushButton_savelog.setStyleSheet("margin: 0rem;")
        self.pushButton_savelog.setCheckable(False)
        self.pushButton_savelog.setDefault(False)
        self.pushButton_savelog.setFlat(False)
        self.pushButton_savelog.setObjectName("pushButton_savelog")
        self.verticalLayout_2.addWidget(self.pushButton_savelog)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 7)
        self.horizontalLayout.setStretch(2, 4)

        self.pushButton_home.clicked.connect(lambda: self.tryNewFunctionality())
        self.pushButton_savelog.clicked.connect(lambda: self.handleSaveLog())
        self.pushButton_settings.clicked.connect(lambda: self.tryNewFunctionality())
        self.pushButton_movement.clicked.connect(lambda: self.addSubWindow("movement"))
        self.pushButton_arm.clicked.connect(lambda: self.addSubWindow("arm"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addSubWindow(self, viewToAdd: str):
        """ Show a subwindow in the MDI central area """

        view = None

        if viewToAdd == "movement":
            view = MovementView()
        elif viewToAdd == "arm":
            view = ArmView()

        if view != None:
            subwindow = self.mdiArea.addSubWindow(view)
            subwindow.setWindowTitle("Example Widget")
            subwindow.show()

    def tryNewFunctionality(self):
        """ Testing """
        print("Prova")
    
    def handleSaveLog(self):
        """ Handles Save Log"""
        print("Handling Save Log")
    

    def set_dc_engine_value(value): 
        """ Returns a value for the DC engine. Highest value: , Lowest value: 255 """
        print (f"DC engine set to: {value}") 
        return value*255


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ASTRA Khonsu"))
        self.label_4.setText(_translate("MainWindow", "ASTRA Khonsu"))
        self.pushButton_home.setText(_translate("MainWindow", "Home"))
        self.pushButton_movement.setText(_translate("MainWindow", "Movement"))
        self.pushButton_arm.setText(_translate("MainWindow", "Arm"))
        self.pushButton_settings.setText(_translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "Bluetooth"))
        self.pushButton_savelog.setText(_translate("MainWindow", "Save Log"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowIcon(QIcon(".\\res\\images\\astra_logo.jpg"))
    MainWindow.setIconSize(QSize(256,256))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # se scommenti esplode tutto
    # obj_astruino = astruino()
    # print(astruino.isAstruinoConnected)

    sys.exit(app.exec_())