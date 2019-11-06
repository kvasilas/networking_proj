#!/bin/bash

nmap command >> RAW

for ((i = 0 ; i < 168 ; i++)); do
  echo "traceroute $i"
    nmao words >> RAW
    awk -f user_parse.awk RAW >> number_users
    #awk -f name_mac.awk TraceData >> numbers
    sleep 60

done

#python for graphing