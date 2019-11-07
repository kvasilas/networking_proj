BEGIN {

}

{
	if($1 == "Nmap" && $2 == "scan")
		    print $5","
    if($1 == "MAC")
    print $3","
} 

END{

}