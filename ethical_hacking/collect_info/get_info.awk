BEGIN {

}

{
    if($1 == "Nmap" && $2 == "scan")
        if(index($5, "192") != 0)
        {
            print "NAME|"$5
            print "IP|"$5
        }
        else
        {
            print "NAME|"$5
            print "IP|"$6
        }    
    else if($1 == "MAC")
        print "MAC|"$3
}

END{

}