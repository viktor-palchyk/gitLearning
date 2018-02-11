def length(element):
    if type(element) == int:
        return "Sorry, integers have no length"
    elif type(element) == float:
        return "Sorry, floats have no length"
    else:
        return len(element)

print(length("asdfasl;djkd als;djfkjlds;kd"))
print(length(2.2))
print(length(0))
