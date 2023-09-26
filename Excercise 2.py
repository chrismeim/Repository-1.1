type = (input("Are you converting celcius to fahrenheit? "))
degrees = int(input("Give me the temperature "))

def converter(x, z):
    if x == "yes":
        f = (z*9/5) + 32
        print(f"{z} degrees Celcius = {f} fahrenheit")
        return f
    else: 
        c = 5/9*(z-32)
        print(f"{z} fahrenheit = {c} celcius degrees")
        return c

x = converter(type, degrees)
