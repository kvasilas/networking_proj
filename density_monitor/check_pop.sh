#!/bin/bash

my_ip=`ip route get 8.8.8.8 | sed -n '/src/{s/.*src *\([^ ]*\).*/\1/p;q}'`

for ((i = 0 ; i < 169 ; i++)); do #169 for plotting only need 168
    date >> time_stamps
    echo $i >> numbers
    nmap -sP $my_ip/24 > RAW
    awk -f host_parse.awk RAW >> number_host.txt
    awk -f ip_parse.awk RAW >> number_ip.txt
    echo $1
    sleep 3600 
done

python3 plotter.py