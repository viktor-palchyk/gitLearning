def currency_converter(rate, euro):
	dollar = rate * euro
	return dollar

r = input("What is the rate? ")
e = input("What is the amount of euros? ")
print("The amount of dollars:", currency_converter(float(r), float(e)))