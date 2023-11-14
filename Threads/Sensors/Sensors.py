#HERE IS A FILE TO HANDLE ALL THE SENSOR DATA INSIDE THE CENTRAL WINDOW
import asyncio
import os
import sys
import time
from asyncio import events

import cv2
from PySide6.QtCore import Qt, QThread, Signal, Slot, QSize
from PySide6.QtGui import QAction, QImage, QKeySequence, QPixmap
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox,
                               QHBoxLayout, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)
from main import *

#initializing the variables
MAC_ADDRESS = "01:23:45:67:A6:31"
ASTRUINO_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"


# ENFF astruino_send_command------------------------------------------------------------


class Astruino(QThread):

    
    def __init__(self, value, parent=None):
        QThread.__init__(self, parent)
        self.args = value
        self.astruino_start = Signal()
        self.astruino_done = Signal()

    def run(self):
        print("Starting communication")

        loop = asyncio.new_event_loop()
        tasks = list()
        tasks.append(loop.create_task(self.astruino_send_command()))
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()

    async def astruino_send_command(self):
        """
        Sends a command to Astruino
        example command: "napoli juve 3"
        """

        res_bytes = self.args

        try:
            async with BleakClient(MAC_ADDRESS) as client:
                await client.write_gatt_char(ASTRUINO_UUID, bytes(res_bytes, 'utf-8'))

                # if self.print_debug_messages:
                #     print(f"just sent: {res_bytes}")

                #     self.append_log(f"just sent: {res_bytes}")
                #     print('signal done')

                self.astruino_done.emit()
                # self.timer_astruino_send_command.stop()
                return
            
        except BleakError as e:
            # TODO Non riesco ad importare l'oggetto Errore corretto
            # Faccio questa porcata per uscirmene in fretta, sistemare dopo

            if str(e).startswith('No powered Bluetooth'):
                # self.pushButton_checkConnession.setEnabled(True)
                pass

            if str(e).startswith('Device with address'):
                # self.pushButton_checkConnession.setEnabled(True)
                pass

            if str(e).startswith('failed to discover'):
                print('Timout detected!')

            print(e)
            # self.append_log(str(e))
            # self.status_bar.showMessage((str(e)))

            # self.set_all_buttons_enabled(False)
            # self.pushButton_checkConnession.setEnabled(True)

            # self.timer_astruino_send_command.stop()
            return

    # def parse_command(self, command: str) -> str:
    #     """
    #         Returns a parsed command
    #         command: str

    #         command="napoli juve 3"
    #         res = "napoli-juve-3"

    #         Choosing # self.args = "aaaaabbbbbaaaaabbbbb" will result in a warning
    #     """

    #     command = command.lower()
    #     res = command.replace(' ', '-')

    #     if len(command) > 18:
    #         print(
    #             f'Warning: parsed command is longer than 18 characters.\nThe command was stripped down from/to\n{command}\n{command[0:18]}'
    #         )
    #         command = command[0:18]

    #     if self.print_debug_messages:
    #         print('command parsed: ', res, ' binary: ', bytes(res, "utf-8"))

    #     # Ho provato a ritornare bytes(res, 'utf-8') ma non funziona
    #     return res