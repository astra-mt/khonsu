from PySide6 import QtCore, QtGui, QtWidgets
from .. import signals

class ArmView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        Form = self
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(581, -10, 581, 763))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(20)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 551, 411))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 10)
        self.formLayout.setVerticalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_3)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_4)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(40, 360, 541, 371))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_grab = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_grab.setObjectName("pushButton_grab")
        self.verticalLayout.addWidget(self.pushButton_grab)
        self.pushButton_move = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_move.setObjectName("pushButton_move")
        self.verticalLayout.addWidget(self.pushButton_move)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setGeometry(QtCore.QRect(5, 1, 581, 741))
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.frame)



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.plainTextEdit, self.plainTextEdit_3)
        Form.setTabOrder(self.plainTextEdit_3, self.plainTextEdit_4)
        Form.setTabOrder(self.plainTextEdit_4, self.plainTextEdit_2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "    x:"))
        self.label_2.setText(_translate("Form", "    y:"))
        self.label_3.setText(_translate("Form", "    z:"))
        self.label_4.setText(_translate("Form", "    θ:"))
        self.pushButton_grab.setText(_translate("Form", "Grab"))
        self.pushButton_move.setText(_translate("Form", "Move"))
