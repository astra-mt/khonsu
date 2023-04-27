import asyncio
import time as t
from bleak import BleakScanner, BleakClient

mac_address = "01:23:45:67:A6:31"
VENDOR_SPECIFIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"
IO_CONFIG_CHAR_UUID = "f000aa66-0451-4000-b000-000000000000"


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

    # Collegato e funzionante :)

    async with BleakClient(mac_address) as client:
        if client.is_connected():
            print("astruino già connesso!")
        else:
            print("astruino non connesso! connessione in corso")
            await client.connect()
            print("astruino connesso!")

        ##

        # for service in client.services:
        #     print(service)
        #     for char in service.characteristics:
        #         print("\t\t", char)

        await client.write_gatt_char(VENDOR_SPECIFIC_UUID, b"napoli juve aperol")

        #res_bytes = await client.read_gatt_char(VENDOR_SPECIFIC_UUID)
        #res = bytearray.decode(res_bytes)
        #print(res)

        t.sleep(5)
        await client.disconnect()
    print("astruino sconnesso!")

asyncio.run(main())
