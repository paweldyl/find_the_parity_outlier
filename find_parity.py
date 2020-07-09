def find_outlier(integers):
	if type(integers) is not list:
		raise ValueError("to nie jest lista.")
	for integer in integers:
		if not isinstance(integer, int):
			raise ValueError("lista zawiera elementy które nie są intami.")
	if len(integers) < 3:
			raise ValueError("lista za krótka! ({})".format(len(integers)))		
	even_counter = 0
	odd_counter = 0
	for integer in integers:
		if integer % 2 == 0:
			even_counter += 1
		else:
			odd_counter += 1
		if even_counter > 1 or odd_counter > 1:
			break
	for integer in integers:
		if even_counter > 1 and integer % 2 != 0:
			return integer
		elif odd_counter > 1 and integer % 2 == 0:
			return integer
	return ValueError("tablica zawiera same parzyste lub nieparzyste liczby.")
