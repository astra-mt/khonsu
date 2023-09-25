import asyncio
from bleak import BleakScanner, BleakClient
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject

# TODO è in chiaro
mac_address = "01:23:45:67:A6:31"
ASTRUINO_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

class Astruino(QObject):

    start_signal = pyqtSignal()
    done_signal = pyqtSignal()

    print_debug_messages = False
    connection_timeout = 2.0

    async def send_command(self, command: str, val: int = None):
        """
            Sends a command to Astruino
            command: "napoli juve"
            <val>: 3
        """
    
        res_bytes = self.parse_command(command, val)

        async with BleakClient(mac_address) as client:
            await client.write_gatt_char(ASTRUINO_UUID, bytes(res_bytes, 'utf-8'))

            # if self.print_debug_messages:
            #     print(f"just sent: {res_bytes}")

        self.done_signal.emit()
        return

    def parse_command(self, command: str, val: float = None) -> str:
        """
            Returns a parsed command
            command: str
            val: float (optional)

            command="napoli juve", val=3
            res = "napoli-juve-3"
        """

        res = command.replace(' ', '-')

        if val:
            return res + '-' + str(val)

        # if self.print_debug_messages:
        #     print('command parsed: ', res, ' binary: ', bytes(res, "utf-8"))

        # Ho provato a ritornare bytes(res, 'utf-8') ma non funziona
        return res


