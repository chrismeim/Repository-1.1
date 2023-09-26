type = (input("Are you converting celcius to fahrenheit? "))
degrees = int(input("Give me the temperature"))

def converter(x, z):
    if x == "yes":
        f = (z*9/5) + 32
        return f
    else: 
        c = 5/9*(z-32)
        return c

x = converter(type, degrees)
