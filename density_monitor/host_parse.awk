BEGIN {

}

{

}

END{
	print substr($6, 2, length($6) - 1)
}