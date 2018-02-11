def celsius_to_fahrenheit(celsius):
	for item in celsius:
		if float(item) < -273.15:
			fahrenheit = "That temperature doesn't make sense!"
		else:
			fahrenheit = item * 9 / 5 + 32
		print(fahrenheit)

temperatures=[10,-20,-289,100]
print(celsius_to_fahrenheit(temperatures))

