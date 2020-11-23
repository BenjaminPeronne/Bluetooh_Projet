# -*- coding: latin -*-

"""
A simple Python script to send messages to a sever over Bluetooth
using PyBluez (with Python 2).
"""

from bluetooth import *

# adresse dongle 00:15:83:4C:1A:DF
# adresse PC-HP-WIN10 F8:28:19:80:77:9E
# adresse rpi3 B8:27:EB:C6:2B:E2
# adresse samsung 5C:51:81:59:9F:FE
# adresse HC-06 98:D3:32:20:50:42

serverMACAddress = "98:D3:32:20:50:42"
port = 1

"""
# Create the client socket
client_socket=BluetoothSocket( RFCOMM )
client_socket.connect((serverMACAddress, port))
print "Client connecte au serveur"

client_socket.send("Hello World'\r'")
print "Finished"
client_socket.close()


"""

client_socket = BluetoothSocket(RFCOMM)
client_socket.connect((serverMACAddress, port))
print "Client connecte au serveur"
while 1:
    text = raw_input("enter le texte a envoyer (quit pour terminer) : ") # Note change to the old (Python 2) raw_input
    client_socket.send(text)
    if text == "quit":
        break
client_socket.close()


