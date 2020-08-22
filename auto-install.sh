#!/bin/bash

#note to use git
#pkg install git


echo "Auto-Install"
echo "This will install metasploit & nmap"

pkg update -y && pkg upgrade -y

termux-setup-storage

pkg install unstable-repo -y

pkg install metasploit -y

pkg install nmap -y

echo "Done with the install!"
