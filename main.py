from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSize, QObject, Signal, Slot, QEvent, QTimer

import os
import cv2
import sys
import time
import signal
import asyncio
import datetime
import qimage2ndarray

from bleak import BleakScanner, BleakClient, BleakError
from .async_helper import AsyncHelper

from .ui.movement import MovementView
from .ui.arm import ArmView


# Informazioni private in chiaro, ma siamo fortunati, soltanto chi
# ha accesso alla repository può causare errori fatali!
# TOOD Soluzione: https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1

CAM_URL = "http://192.168.1.18"
MAC_ADDRESS = "01:23:45:67:A6:31"
ASTRUINO_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

SAVELOG_PATH = os.getcwd()


class Ui_MainWindow(QtWidgets.QMainWindow):

    video_size = QSize(320, 240)

    astruino_start = Signal()
    astruino_done = Signal()

    print_debug_messages = True
    args = ""  # arguments in astruino_send_command

    old_image = None

    def __init__(self):
        super().__init__()

        are_all_buttons_enabled = True

        self.setWindowIcon(
            QIcon(os.path.join("khonsu", "res", "images", "logo.svg")))
        self.setIconSize(QSize(256, 256))

        Form = QtWidgets.QWidget(self)
        Form.setObjectName("MainWindow")
        # Form.resize(1044, 594)
        self.setCentralWidget(Form)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Il fatto di usare QLabel è temporaneo
        self.videoWidget = QtWidgets.QLabel(Form)
        # self.videoWidget.setText('Video Output not yet implemented')
        # self.videoWidget.setAlignment(QtCore.Qt.AlignCenter)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.videoWidget.sizePolicy().hasHeightForWidth())
        # self.videoWidget.setSizePolicy(sizePolicy)
        # self.videoWidget.setMinimumSize(QtCore.QSize(512, 512))
        self.videoWidget.setObjectName("videoWidget")
        self.horizontalLayout.addWidget(self.videoWidget)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 298, 574))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_battery = QtWidgets.QLabel(self.frame)
        self.label_battery.setObjectName("label_battery")
        self.gridLayout.addWidget(self.label_battery, 1, 0, 1, 1)
        self.pushButton_checkConnession = QtWidgets.QPushButton(self.frame)
        self.pushButton_checkConnession.setObjectName(
            "pushButton_checkConnession")
        self.gridLayout.addWidget(self.pushButton_checkConnession, 2, 0, 1, 1)
        self.label_icon = QtWidgets.QLabel(self.frame)
        self.label_icon.setObjectName("label_icon")
        self.gridLayout.addWidget(self.label_icon, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.textBrowser = QtWidgets.QTextBrowser(
            self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton_saveLog = QtWidgets.QPushButton(
            self.scrollAreaWidgetContents)
        self.pushButton_saveLog.setObjectName("pushButton_saveLog")
        self.verticalLayout.addWidget(self.pushButton_saveLog)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.toolBox = QtWidgets.QToolBox(self.scrollAreaWidgetContents)
        self.toolBox.setObjectName("toolBox")
        self.movementWidget = MovementView()
        self.movementWidget.setObjectName("MovementView")
        self.toolBox.addItem(self.movementWidget, "")
        self.armWidget = ArmView()
        self.armWidget.setObjectName("armWidget")
        self.toolBox.addItem(self.armWidget, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.verticalLayout.addWidget(self.toolBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)

        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.setObjectName('statusBar')
        self.status_bar.showMessage('Welcome back!')

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # signal: true -> enables buttons, false -> disables buttons

        # # Astruino fa qualcosa santodio
        self.movementWidget.pushButton_go.clicked.connect(
            lambda: self.handle_pushButton_movement(
                self.movementWidget.spinBox_rpm.value())
        )

        self.movementWidget.pushButton_stop.clicked.connect(
            lambda: self.handle_pushButton_movement(0)
        )

        # self.pushButton_checkConnession.clicked.connect(
        #     # lambda: asyncio.run(self.handle_pushButton_checkConnession())
        # )

        self.pushButton_saveLog.clicked.connect(
            lambda: self.handle_pushButton_saveLog()
        )

    def handle_pushButton_movement(self, val):
        if self.print_debug_messages:
            print('handle movement')

        self.args = "movement " + str(val)
        self.async_start()

    async def handle_pushButton_checkConnession(self):
        self.status_bar.showMessage('Checking Astruino Connection')

        self.set_all_buttons_enabled(False)

        try:
            async with BleakClient(MAC_ADDRESS) as client:
                await client.write_gatt_char(ASTRUINO_UUID, bytes(res_bytes, 'utf-8'))
        except BleakError as e:
            # TODO Write error to LOG as well
            print(e)
            self.status_bar.showMessage(str(e))
            self.set_all_buttons_enabled(False)

        self.pushButton_checkConnession.setEnabled(True)

    def handle_pushButton_saveLog(self):
        self.status_bar.showMessage('Saving file log')

        t = time.localtime()
        current_time = time.strftime("%D_%H%M%S", t)
        current_time = current_time.replace('/', '')
        # print(current_time)

        path = os.path.join(SAVELOG_PATH, "logs")

        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as e:
                print(e)

        if os.path.exists(path):
            path = os.path.join(path, f"log_{current_time}")
            log_file = open(path, "x")
            log_file.write(
                'prova123'
            )

            self.status_bar.showMessage(f'Log written, open {path}')

            print('TODO File scritto con successo ma è inutile')

    def set_all_buttons_enabled(self, var: bool):
        """
            Sets all buttons that could trigger astruino_send_command to value var.
            var: True -> enables all buttons
            var: False -> disables all buttons
        """

        # TODO (REDO)
        # look im desperate dont judge. quick and dirty solution.
        # i just wanna focus on more serious stuff asap

        # list of objects that call astruino_send_command
        objects = [
            self.movementWidget.pushButton_go,
            self.movementWidget.pushButton_stop,
            self.pushButton_checkConnession,
            self.armWidget.pushButton_armGrab,
            self.armWidget.pushButton_armMove,
        ]

        for obj in objects:
            obj.setEnabled(var)

        # if not var:
        #     self.status_bar.showMessage('Sending command to Astruino')
        # else:
        #     self.status_bar.showMessage('Astruino ready to send')

    def setup_camera(self):
        """
            Initialize camera.
        """

        self.capture = cv2.VideoCapture(CAM_URL + ":81/stream")
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        self.timer = QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start(5)

        # TODO Implement two buttons for the camera
        # You can start and stop the video stream by using self.timer.start(number) and self.timer.stop()

    def display_video_stream(self):
        """
            Read frame from camera and repaint QLabel widget.
            Awfully dirty solution
        """

        # TODO there must be a better way to do this ...

        _, frame = self.capture.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        image = qimage2ndarray.array2qimage(frame)  # SOLUTION FOR MEMORY LEAK
        
        if image is not self.old_image:
            self.videoWidget.setPixmap(QPixmap.fromImage(image))

        self.old_image = image

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_battery.setText(_translate("MainWindow", "Battery"))
        self.pushButton_checkConnession.setText(
            _translate("MainWindow", "Check Connession"))
        self.label_icon.setText(_translate("MainWindow", "Icon"))
        self.pushButton_saveLog.setText(_translate("MainWindow", "Save Log"))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.movementWidget), _translate("MainWindow", "Movement"))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.armWidget), _translate("MainWindow", "Arm"))
        self.toolBox.setItemText(self.toolBox.indexOf(
            self.page_3), _translate("MainWindow", "Page 3"))

    @Slot()
    def async_start(self):
        self.astruino_start.emit()
        if self.print_debug_messages:
            print('signal start')

        self.set_all_buttons_enabled(False)

    async def astruino_send_command(self):
        """
        Sends a command to Astruino
        example command: "napoli juve 3"
        calls parse_command() and sends b"napoli-juve-3" to Astruino
        """

        res_bytes = self.parse_command(self.args)

        async with BleakClient(MAC_ADDRESS) as client:
            await client.write_gatt_char(ASTRUINO_UUID, bytes(res_bytes, 'utf-8'))

            if self.print_debug_messages:
                print(f"just sent: {res_bytes}")
                print('signal done')

            self.astruino_done.emit()

    def parse_command(self, command: str) -> str:
        """
            Returns a parsed command
            command: str

            command="napoli juve 3"
            res = "napoli-juve-3"


            Choosing # self.args = "aaaaabbbbbaaaaabbbbb" will result in a warning
        """

        command = command.lower()
        res = command.replace(' ', '-')

        if len(command) > 18:
            print(
                f'Warning: parsed command is longer than 18 characters.\nThe command was stripped down from/to\n{command}\n{command[0:18]}'
            )
            command = command[0:18]

        if self.print_debug_messages:
            print('command parsed: ', res, ' binary: ', bytes(res, "utf-8"))

        # Ho provato a ritornare bytes(res, 'utf-8') ma non funziona
        return res


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    async_helper = AsyncHelper(ui, ui.astruino_send_command)
    ui.set_all_buttons_enabled(False)
    ui.pushButton_checkConnession.setEnabled(True)
    ui.show()
    ui.setup_camera()

    # No clue what this does, don't touch.
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    sys.exit(app.exec())
