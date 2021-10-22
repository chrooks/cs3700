#!/usr/bin/env python3

import struct, socket

nm = "255.255.255.0"

x = bin(struct.unpack('!I', socket.inet_aton(nm))[0])[2:]

print(x)
    
print(x.count('1'))