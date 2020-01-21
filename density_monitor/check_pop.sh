#!/bin/bash

my_ip=""

for ((i = 0 ; i < 169 ; i++)); do #169 for plotting only need 168
    date >> time_stamps
    echo $i >> numbers
    nmap -sP 192.168.1.0/24 > RAW
    awk -f host_parse.awk RAW >> number_host.txt
    awk -f ip_parse.awk RAW >> number_ip.txt
    echo $1
    sleep 3600 
done

python3 plotter.py