def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Sorry, too low temperature"
    else:
        return celsius*9.5 + 32

print((celsius_to_fahrenheit(3)))
print((celsius_to_fahrenheit(-2234)))
