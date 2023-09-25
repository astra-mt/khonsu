# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# Docs: https://doc.qt.io/qtforpython-6/examples/example_async_minimal.html


# from bluetooth.astruino import Astruino
from PySide6.QtCore import (Qt, QEvent, QObject, Signal, Slot)
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)

from bleak import BleakScanner, BleakClient

import asyncio
import signal
import sys

import random
import string

# TODO è in chiaro
mac_address = "01:23:45:67:A6:31"
ASTRUINO_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"


class MainWindow(QMainWindow):

    start_signal = Signal()
    done_signal = Signal()
    # astruino = Astruino()
    args = ""

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)

        self.text = QLabel("The answer is 42.")
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)

        async_trigger1 = QPushButton(text="Button 1")
        async_trigger2 = QPushButton(text="Button 2")
        # self.args = "napoli juve 3"

        async_trigger1.clicked.connect(lambda: self.handle_button_1())
        async_trigger2.clicked.connect(lambda: self.handle_button_2())

        layout.addWidget(
            async_trigger1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(
            async_trigger2, alignment=Qt.AlignmentFlag.AlignCenter)

    def handle_button_1(self):
        self.args = "napoli juve 3"
        self.async_start()

    def handle_button_2(self):
        self.args = "sangue cazzo"
        self.async_start()

    @Slot()
    def async_start(self):
        self.start_signal.emit()

    async def astruino_send_command(self):
        """
        Sends a command to Astruino
        command: "napoli juve 3"
        """

        res_bytes = self.parse_command(self.args)

        async with BleakClient(mac_address) as client:
            await client.write_gatt_char(ASTRUINO_UUID, bytes(res_bytes, 'utf-8'))

            # if self.print_debug_messages:
            #     print(f"just sent: {res_bytes}")

        self.done_signal.emit()

    def parse_command(self, command: str) -> str:
        """
            Returns a parsed command
            command: str

            command="napoli juve 3"
            res = "napoli-juve-3"
        """

        res = command.replace(' ', '-')

        # if self.print_debug_messages:
        #     print('command parsed: ', res, ' binary: ', bytes(res, "utf-8"))

        # Ho provato a ritornare bytes(res, 'utf-8') ma non funziona
        return res


class AsyncHelper(QObject):

    class ReenterQtObject(QObject):

        def event(self, event):
            if event.type() == QEvent.Type.User + 1:
                event.fn()
                return True
            return False

    class ReenterQtEvent(QEvent):

        def __init__(self, fn):
            super().__init__(QEvent.Type(QEvent.Type.User + 1))
            self.fn = fn

    def __init__(self, worker, entry):
        super().__init__()
        self.reenter_qt = self.ReenterQtObject()
        self.entry = entry
        self.loop = asyncio.new_event_loop()
        self.done = False

        self.worker = worker
        if hasattr(self.worker, "start_signal") and isinstance(self.worker.start_signal, Signal):
            self.worker.start_signal.connect(self.on_worker_started)
        if hasattr(self.worker, "done_signal") and isinstance(self.worker.done_signal, Signal):
            self.worker.done_signal.connect(self.on_worker_done)

    @Slot()
    def on_worker_started(self):
        if not self.entry:
            raise Exception(
                "No entry point for the asyncio event loop was set.")
        asyncio.set_event_loop(self.loop)
        self.loop.create_task(self.entry())
        self.loop.call_soon(self.next_guest_run_schedule)
        # Set this explicitly as we might want to restart the guest run.
        self.done = False
        self.loop.run_forever()

    @Slot()
    def on_worker_done(self):
        self.done = True
        print('signal_done')

    def continue_loop(self):
        if not self.done:
            self.loop.call_soon(self.next_guest_run_schedule)
            self.loop.run_forever()

    def next_guest_run_schedule(self):
        self.loop.stop()
        QApplication.postEvent(
            self.reenter_qt, self.ReenterQtEvent(self.continue_loop))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()

    async_helper = AsyncHelper(main_window, main_window.astruino_send_command)

    main_window.show()

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app.exec()
