import random
y = True   #dummy variable

while y == True:
    guess_number = int(input("Take a guess"))
    if guess_number == random.randint(1,9):
        print("You got it")
        y = False
