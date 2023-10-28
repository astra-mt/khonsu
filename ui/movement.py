from PySide6 import QtCore, QtGui, QtWidgets
from .. import signals


class MovementWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        Form = self
        Form.setObjectName("MovementWidget")
        Form.setAccessibleName("MovementWidget")
        # Form.resize(512, 512)
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
        self.dial.setMaximum(255)
        self.dial.setMinimum(0)
        self.verticalLayout.addWidget(self.dial)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spinBox_rpm = QtWidgets.QSpinBox(self.frame)
        # self.spinBox_rpm.('100')
        self.spinBox_rpm.setObjectName("spinBox_rpm")
        self.spinBox_rpm.setRange(0, 255)
        self.horizontalLayout.addWidget(self.spinBox_rpm)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButton_go = QtWidgets.QPushButton(self.frame)
        self.pushButton_go.setObjectName("pushButton_go")
        self.pushButton_go.setDisabled(True)
        self.verticalLayout.addWidget(self.pushButton_go)
        self.pushButton_stop = QtWidgets.QPushButton(self.frame)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.dial.valueChanged.connect(
            lambda: self.handle_valueChanged_dial()
        )

        self.spinBox_rpm.valueChanged.connect(
            lambda: self.dial.setValue(self.spinBox_rpm.value())
        )
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def handle_valueChanged_dial(self):
        val = self.dial.value()
        self.spinBox_rpm.setValue(signals.set_rpm_value(val))

        if not val:
            self.pushButton_go.setDisabled(True)
        else:
            self.pushButton_go.setDisabled(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "RPM"))
        self.pushButton_go.setText(_translate("Form", "Go"))
        self.pushButton_stop.setText(_translate("Form", "Stop"))