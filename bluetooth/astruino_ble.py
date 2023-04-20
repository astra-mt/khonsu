import asyncio
# import time as t
from bleak import BleakScanner, BleakClient

mac_address="01:23:45:67:A6:31"

async def main():
    # devices = await BleakScanner.discover()
    # for d in devices:
    #     print(d)

    astruino = await BleakScanner.find_device_by_name('astruino', timetout=5.0);
    if astruino:
        print(astruino)
    else:''
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

        # non so cosa sia
        # https://bleak.readthedocs.io/en/latest/api/client.html
        char_specifier = {client.services, }     
        data = {}
        response = False;           
        await client.read_gatt_char(char_specifier: [client.services, ]);

        # t.sleep(20);
        await client.disconnect()
        print("astruino sconnesso!")

asyncio.run(main())
