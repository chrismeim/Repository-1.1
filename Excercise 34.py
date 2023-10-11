x = int(input("Give me number 1 "))
y = int(input("Give me number 2 "))

def summation(number1, number2):
    if 15 <= number1 + number2 <= 20:
        output = 20
    else:
        output = number1 + number2   
    
    print(output)

summation(x, y)