def max_integer(my_list=[]):
    max_number = 0
	
    if my_list:
	for number in my_list:
	    if number > max_number:
		max_number = number
	return max_number
    else:
	return None
