
import nmap, os
#PART1# Alocarea variabilelor

obiect=nmap.PortScanner()
port='20-80'
devices=''

#PART2# Obtinerea device-urilor din retrea

print("Getting devices from network..")
devices=os.popen(' arp -n | cut -f1 -d \' \' | grep [0-9]').read()

#PART3# Formatarea datelor pentru procesare 

devices=devices.split("\n")
devices.append[:-1]

#PART4#Scanarea adreselor IP

print("Waiting to scan...")
nr=1
for ip in devices:
	print("Scaning devices "+ str(nr))
	res=obiect.scan(ip,port)
	print(res)
	nr=nr+1
print("Scan is done!")