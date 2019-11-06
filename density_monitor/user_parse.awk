BEGIN {

}

{
	#if($1 == 64)
	#	split($(NF-1), data, "=")
	#	print data[2]
} 

END{
    print $(6)
}