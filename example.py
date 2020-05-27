#!/bin/python
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True, lookup_class)
print("Found {} devices.".format(len(nearby_devices)))
print(nearby_devices)

for addr, name in nearby_devices:
  print(" {} - {}".format(addr, name))

