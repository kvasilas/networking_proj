#!/bin/bash

my_ip=`ip route get 8.8.8.8 | sed -n '/src/{s/.*src *\([^ ]*\).*/\1/p;q}'`
nmap -sP $my_ip/24 > RAW
awk -f get_info.awk RAW > devices

