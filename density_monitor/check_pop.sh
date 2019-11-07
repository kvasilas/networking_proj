#!/bin/bash

for ((i = 0 ; i < 169 ; i++)); do #169 for plotting only need 168
    date >> data/time_stamps
    echo $i >> data/numbers
    nmap -sP 192.168.1.0/24 > data/RAW
    awk -f host_parse.awk RAW >> data/number_host.txt
    awk -f ip_parse.awk RAW >> data/number_ip.txt
    sleep 3600 
done

#python3 plotter.py