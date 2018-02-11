def celsius_to_fahrenheit(celsius):
	file = open("c2f_conversion.txt", "w")
	for item in celsius:
		if float(item) < -273.15:
			fahrenheit = "That temperature doesn't make sense!"
			print(fahrenheit)
		else:
			fahrenheit = item * 9 / 5 + 32
			file.write(str(fahrenheit)+'\n')
			print(str(fahrenheit)+" has been written into file")
	file.close()

temperatures=[10,-20,-289,100]
print(celsius_to_fahrenheit(temperatures))

