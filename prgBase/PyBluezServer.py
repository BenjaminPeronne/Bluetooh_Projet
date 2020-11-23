# -*- coding: latin -*-

"""
A simple Python script to receive messages from a client over
Bluetooth using PyBluez (with Python 2).
"""

from bluetooth import *

# adresse dongle 00:15:83:4C:1A:DF
# adresse PC-HP-WIN10 F8:28:19:80:77:9E
# adresse rpi3 B8:27:EB:C6:2B:E2
# adresse samsung 5C:51:81:59:9F:FE
# adresse HC-06 98:D3:32:20:50:42

hostMACAddress = "F8:28:19:80:77:9E" # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 10


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind((hostMACAddress,port))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )
               
print "Waiting for connection on RFCOMM channel %d" % port

client_sock, client_adresse = server_sock.accept()
print "Accepted connection from ", client_adresse

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
            break
        print "received [%s]" % data
except IOError:
    print "erreur"
    pass

print "disconnected"

client_sock.close()
server_sock.close()
print "all done"


"""

backlog = 1
size = 1024
s = BluetoothSocket(RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    print "Serveur connecte au client"
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
except:	
    print "Closing socket"
    client.close()
    s.close()

"""
