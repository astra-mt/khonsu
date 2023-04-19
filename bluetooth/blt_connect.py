import bluetooth
import threading
import socket

""" for count in range(1,10):
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print(nearby_devices)

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect(("01:23:45:67:A6:31", port))
sock.send("hello!!")
sock.close()
"""

serverMACAddress = '01:23:45:67:A6:31'

port = 3
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
""" while 1:
    text = input()
    if text == "quit":
        break
    s.send(bytes(text, 'UTF-8')) """
s.send(bytes('a', 'UTF-8'))
s.close()