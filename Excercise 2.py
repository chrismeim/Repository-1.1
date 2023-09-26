type_of_conversion = (input("Are you converting celcius to fahrenheit? "))
degrees = int(input("Give me the temperature "))

def converter(input_of_convesrion, input_of_degrees):
    if input_of_convesrion == "yes":
        fahrenheit = (input_of_degrees*9/5) + 32
        print(f"{input_of_degrees} degrees Celcius = {fahrenheit} fahrenheit")
        return fahrenheit
    else: 
        celcius = 5/9*(input_of_degrees-32)
        print(f"{input_of_degrees} fahrenheit = {celcius} celcius degrees")
        return celcius

x = converter(type_of_conversion, degrees)
