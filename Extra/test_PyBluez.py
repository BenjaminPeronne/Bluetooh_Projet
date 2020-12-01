# -*- coding: latin -*-
from bluetooth import *

"""
print "Test n°1 : performing inquiry ..."
nearby_devices = discover_devices(lookup_names = True)
print "found %d devices" % len(nearby_devices)

for name, addr in nearby_devices:
     print " %s - %s" % (addr, name)
"""	 


print "Test n°2 : find device by name ..."
target_name = "Interstellar"
target_address = None

nearby_devices = discover_devices()

for bdaddr in nearby_devices:
    if target_name == lookup_name( bdaddr ):
        target_address = bdaddr
        break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"
