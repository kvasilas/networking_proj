#!/bin/bash

addr1="www.website.com"
addr2="www.website.com"

for ((i = 0 ; i < 168 ; i++)); do
    date >> time_stamps
    #do the dns thing
    #dig @1.1.1.1 +norecurse $addr1 > data1
    #do the parsing thing
    awk -f fileName.awk data1 >> site1_results.txt
    sleep 60
done

#dns query
#resolve ip to mac
#agragate data