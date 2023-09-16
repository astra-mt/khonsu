import asyncio
import time as t
from bleak import BleakScanner, BleakClient
from .. import signals

# TODO porco dio è in chiaro
mac_address = "01:23:45:67:A6:31"
VENDOR_SPECIFIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
IO_CONFIG_CHAR_UUID = "f000aa66-0451-4000-b000-000000000000"

# by far the worst class i've ever written in my entire life


class Astruino:
    isAstruinoConnected = False             # class attribute
    print_debug_messages = True             # self explicatory
    connection_timeout = 2.0

    # def __init__(self):
    #     pass

    async def send_command(self, command: str, val: int = None):
        """
            Sends a command to Astruino
            command: "napoli juve"
            <val>: 3
        """

        # if self.print_debug_messages:
        #     print(f"about to send {command}, {val}")

        res_bytes = self.parse_command(command, val)

        async with BleakClient(mac_address) as client:
            await client.write_gatt_char(VENDOR_SPECIFIC_UUID, bytes(res_bytes, 'utf-8'))

            # if self.print_debug_messages:
            #     print(f"just sent: {res_bytes}")

        return

    def parse_command(self, command: str, val: float = None) -> str:
        """
            Returns the bytes sequence of a command
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

        # Ho provato a ritornare bytes(res, 'utf-8') ma boh non funziona
        return res