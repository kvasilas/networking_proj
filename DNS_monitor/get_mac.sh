#!/bin/bash

#grab the mac addresses and user names associated with them
#stored in csv
nmap -sP 192.168.1.0/24 > RAW
awk -f name_mac.awk RAW >> mac_name
