import asyncio
import time as t
from bleak import BleakScanner, BleakClient
import signals

# TODO porco dio è in chiaro
mac_address = "01:23:45:67:A6:31"
VENDOR_SPECIFIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
IO_CONFIG_CHAR_UUID = "f000aa66-0451-4000-b000-000000000000"

# by far the worst class i've ever written in my entire life

class astruino:
    isAstruinoConnected = False     # class attribute    
    print_debug_messages = True             # self explicatory
    connection_timeout = 2.0

    def __init__(self):
        if self.print_debug_messages:
            print(f"Initializing astruino")

        asyncio.run(self.start_connection())

        if self.print_debug_messages:
            print(f"Initialization done. Connection: {self.isAstruinoConnected}")

        return

    async def start_connection(self):
        astruino = await BleakScanner.find_device_by_name('astruino', timetout=self.connection_timeout)
        
        if self.print_debug_messages:
            if astruino:
                print(astruino)
                print("Astruino connesso!")
            else:
                print(f"Connection timeout ({self.connection_timeout}s) - Astruino non connesso")
                return

        # Collegato e funzionante :)
        async with BleakClient(mac_address) as client:
                if self.print_debug_messages:
                    if client.is_connected():
                        print("Astruino già connesso!")
                    else:
                        print("Astruino non connesso! connessione in corso")
                        await client.connect()
                        print("astruino connesso!")

                self.isAstruinoConnected = client.is_connected()

                # for service in client.services:
                #     print(service)
                #     for char in service.characteristics:
                #         print("\t\t", char)

                # await client.write_gatt_char(VENDOR_SPECIFIC_UUID, b"napoli juve aperol")

                #res_bytes = await client.read_gatt_char(VENDOR_SPECIFIC_UUID)
                #res = bytearray.decode(res_bytes)
                #print(res)

                t.sleep(5)
                await client.disconnect()

                if self.print_debug_messages:
                    print("Astruino sconnesso!")
        
    
    # async def close_connection():
    #     return

    async def main():
        # devices = await BleakScanner.discover()
        # for d in devices:
        #     print(d)

        astruino = await BleakScanner.find_device_by_name('astruino', timetout=5.0)
        
        if self.print_debug_messages:
            if astruino:
                print(astruino)
            else:
                print("non funziona yolo")
                return

        isAstruinoConnected = client.is_connected()
        # Collegato e funzionante :)

        async with BleakClient(mac_address) as client:
            if self.print_debug_messages:
                if client.is_connected():
                    print("Astruino già connesso!")
                else:
                    print("Astruino non connesso! connessione in corso")
                    await client.connect()
                    print("astruino connesso!")

            # for service in client.services:
            #     print(service)
            #     for char in service.characteristics:
            #         print("\t\t", char)

            # await client.write_gatt_char(VENDOR_SPECIFIC_UUID, b"napoli juve aperol")

            # res_bytes = await client.read_gatt_char(VENDOR_SPECIFIC_UUID)
            # res = bytearray.decode(res_bytes)
            # print(res)

            t.sleep(5)
            await client.disconnect()
        if self.print_debug_messages:
            print("Astruino sconnesso!")

    async def send_command(instruction, val):
        """ Sto scrivendo codice senza arduino e circuito elettronico, non ho idea se ciò funzionerà"""

        command = parse_command(command, val)
        await client.write_gatt_char(VENDOR_SPECIFIC_UUID, command)

        if self.print_debug_messages:
            print('just sent: ', command)
        
        return

    async def testAstruino():
        async with BleakClient(mac_address) as client:
            if self.print_debug_messages:
                if not client.is_connected():
                    print("This should not fucking happen")
                    return
            
            if self.print_debug_messages:
                for service in client.services:
                    print(service)
                    for char in service.characteristics:
                        print("\t\t", char)

            await send_command('napoli juve', 3)

            # example_command = parse_command('napoli juve', 3)
            # await client.write_gatt_char(VENDOR_SPECIFIC_UUID, example_command)

            if self.print_debug_messages:
                print('finished writing')

            res_bytes = await client.read_gatt_char(VENDOR_SPECIFIC_UUID)
            res = bytearray.decode(res_bytes)

            if self.print_debug_messages:
                print('message received: ', res)
            

            t.sleep(5)
            if self.print_debug_messages:
                print('sleep done')
        return

    
    def parse_command(command: str, val: float=None):
        """
            Returns the bytes sequence of a command
            command: str
            val: float (optional)

            command="napoli juve", val=3
            res = "napoli-juve-3"
        """
        
        res = command.replace(' ', '-')

        if val:
            return res + str(val)
        
        if self.print_debug_messages:
            print('command parsed: ', res, ' binary: ', bytes(res, "utf-8"))

        return bytes(res, "utf-8")