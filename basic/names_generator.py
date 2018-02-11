import random, string

letter_input

def names_gen():
	"""
	This program will create the names of 3 letters randomly
	"""
	letter1 = random.choice(string.ascii_lowercase)
	letter2 = random.choice(string.ascii_lowercase)
	letter3 = random.choice(string.ascii_lowercase)
	name = letter1 + letter2 + letter3
	return name

print(names_gen())
			