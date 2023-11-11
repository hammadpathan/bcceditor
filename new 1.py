import sys
import os
import codecs

val = int(45000)
catfoodamnthex = hex(val)[2:]
print(catfoodamnthex)
four2 = bytes.fromhex((catfoodamnthex)[-2::1])#.decode('ISO-8859-1')
print(four2)
input()