from PySide6 import QtCore, QtGui, QtWidgets
# from .. import signals


class ArmWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        Form = self
        Form.setObjectName("ArmWidget")
        Form.setAccessibleName("ArmWidget")
        # Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("x")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton_armMove = QtWidgets.QPushButton(Form)
        self.pushButton_armMove.setObjectName("pushButton_armMove")
        self.verticalLayout.addWidget(self.pushButton_armMove)
        self.pushButton_armGrab = QtWidgets.QPushButton(Form)
        self.pushButton_armGrab.setObjectName("pushButton_armGrab")
        self.verticalLayout.addWidget(self.pushButton_armGrab)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton_armMove.setText(_translate("Form", "Move"))
        self.pushButton_armGrab.setText(_translate("Form", "Grab"))
