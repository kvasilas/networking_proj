#!/bin/bash


for ((i = 0 ; i < 168 ; i++)); do
  echo "traceroute $i"
    nmap words >> RAW
    awk -f host_parse.awk RAW >> number_host
    awk -f ip_parse.awk RAW >> number_ip
    #awk -f name_mac.awk TraceData >> mac_name
    sleep 60

done

#python for graphing