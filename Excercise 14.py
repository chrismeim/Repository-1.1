string = input("What is the phrase? ")

list(string)
numbers = 0
characters = 0
spaces = 0

for i in range(len(string)):
    if '0' <= string[i] <= '9':
        numbers +=1
    elif string[i] == " ":
        spaces += 1
    else:
        characters += 1

print(f"The number of characters, numbers and spaces are {characters}, {numbers}, {spaces}")