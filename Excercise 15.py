password = input("What is the password? ")
list(password)

lower_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","0y","z"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]
Upper_letters = [] #creates the Upper_letters list 
for i in lower_letters:  
    Upper_letters.append(i.upper())
    
special_characters = ["$", "#", "@"]


length_variable = 0
length_variable = 0
lower_variable = 0
Upper_variable = 0
special_variable = 0
numbers_variable = 0

if 6 <= len(password) <= 16:  #checks the length of password
    length_variable =1

for i in range(len(password)):  # this loop checks if an Upper and a lower case character exist. Also checks if we have a number from 1-9 and a special character
    for j in range(len(lower_letters)):
        if password[i] == lower_letters[j]:
            lower_variable =1
    for a in range(len(Upper_letters)):
        if password[i] == Upper_letters[a]:
            Upper_variable = 1
    for k in range(len(special_characters)):
        if password[i] == special_characters[k]:
            special_variable = 1
    for l in range(len(numbers)):
        if password[i] == numbers[l]:
            numbers_variable = 1

Test = length_variable + lower_variable + Upper_variable + special_variable + numbers_variable + 
Test

if Test < 5:
    print("The Password is not correct ")
else:
    print("The password is correct")
    