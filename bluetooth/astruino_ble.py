import asyncio
import time as t
from bleak import BleakScanner, BleakClient

mac_address = "01:23:45:67:A6:31"
VENDOR_SPECIFIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
IO_CONFIG_CHAR_UUID = "f000aa66-0451-4000-b000-000000000000"

# by far the worst class i've ever written in my entire life
class astruino:
    isAstruinoConnected = False     # class attribute

    def __init__(self):
        print(f"Initializing astruino. isAstruinoConnected: {isAstruinoConnected}")
        asyncio.run(self.start_connection())
        print(f"Initialization done. isAstruinoConnected: {isAstruinoConnected}")
        return

    async def start_connection(self):
        astruino = await BleakScanner.find_device_by_name('astruino', timetout=3.0)
        if astruino:
            print(astruino)
            print("Astruino connesso!")
        else:
            print("Astruino non connesso")
            return

        # Collegato e funzionante :)
        async with BleakClient(mac_address) as client:
                if client.is_connected():
                    print("Astruino già connesso!")
                else:
                    print("Astruino non connesso! connessione in corso")
                    await client.connect()
                    print("astruino connesso!")

                isAstruinoConnected = client.is_connected()

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
                print("Astruino sconnesso!")
        
    
    # async def close_connection():
    #     return

    async def main():
        # devices = await BleakScanner.discover()
        # for d in devices:
        #     print(d)

        astruino = await BleakScanner.find_device_by_name('astruino', timetout=5.0)
        
        if astruino:
            print(astruino)
        else:
            print("non funziona yolo")
            return

        isAstruinoConnected = client.is_connected()
        # Collegato e funzionante :)

        async with BleakClient(mac_address) as client:
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

            #res_bytes = await client.read_gatt_char(VENDOR_SPECIFIC_UUID)
            #res = bytearray.decode(res_bytes)
            #print(res)

            t.sleep(5)
            await client.disconnect()
        print("Astruino sconnesso!")

    async def sendCommand(command):
        """ Sto scrivendo codice senza arduino e circuito elettronico, non ho idea se ciò funzionerà"""
        await client.write_gatt_char(VENDOR_SPECIFIC_UUID, command.encode('utf-8'))
        print(f"Sto per inviare")
        print(command.encode('utf-8'))
        return

    # if __name__ == "__main__":
    #     asyncio.run(main())
    #     return

    async def testAstruino():
        async with BleakClient(mac_address) as client:
            if not client.is_connected():
                print("This should not fucking happen")
                return
            
            for service in client.services:
                print(service)
                for char in service.characteristics:
                    print("\t\t", char)

            await client.write_gatt_char(VENDOR_SPECIFIC_UUID, b"napoli juve aperol")

            res_bytes = await client.read_gatt_char(VENDOR_SPECIFIC_UUID)
            res = bytearray.decode(res_bytes)
            print(res)

            t.sleep(5)
            
        return
