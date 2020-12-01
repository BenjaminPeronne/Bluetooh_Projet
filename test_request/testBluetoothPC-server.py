# -*- coding: cp1252 -*-
from bluetooth import *

# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# modified by: Benjamin Peronne
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $


server_sock=BluetoothSocket( RFCOMM ) #définit le service de communication 



server_sock.bind(("d0:57:7b:0e:61:62",PORT_ANY)) #adresse mac de l'ordinateur serveur & port
port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )

            
server_sock.listen(1)

print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_adresse = server_sock.accept()
print("Accepted connection from ", client_adresse)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0:
            break
        print("received %s" % data)
        client_sock.send("toto")
except IOError:
    print "erreur"
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
