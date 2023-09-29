my_list=[]
numbers=[]
for i in range(100,401): #through this loop I insert all numbers from 100 to 400 into the variable numbers
    numbers.append(i)


for i in range(len(numbers)): #through this loop I intend to check each individual number if it meets the criteria of the algorithm
    string = str(numbers[i])  # I convert the individual number from the list "my numbers" into a string in order to check each individual item within it
    checker =0
    for j in range(len(string)):  #Through this loop I check each individual digit of the initial number
        if int(string[j])%2 != 0: 
            break
        else:
            checker +=1
    if checker == len(string):   # Here if my number has all its digits meeting the criteria I append it to "my_list" which is a list containing all the numbers in the format
        my_list.append(numbers[i])

print(my_list)