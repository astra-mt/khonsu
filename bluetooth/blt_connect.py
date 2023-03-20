import bluetooth
import threading

for count in range(1,10):
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print(nearby_devices)

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("", port))
sock.send("hello!!")
sock.close()
