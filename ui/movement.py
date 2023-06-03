from PyQt5 import QtCore, QtGui, QtWidgets


class MovementView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        Form = self
        Form.setObjectName("Movement")
        Form.resize(710, 595)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dial = QtWidgets.QDial(self.frame)
        self.dial.setObjectName("dial")
        self.verticalLayout.addWidget(self.dial)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.goButton = QtWidgets.QPushButton(self.frame)
        self.goButton.setObjectName("goButton")
        self.verticalLayout.addWidget(self.goButton)
        self.stopButton = QtWidgets.QPushButton(self.frame)
        self.stopButton.setObjectName("stopButton")
        self.verticalLayout.addWidget(self.stopButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "RPM"))
        self.goButton.setText(_translate("Form", "Go"))
        self.stopButton.setText(_translate("Form", "Stop"))