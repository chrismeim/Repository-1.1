import numpy as np

m = int(input("Give me the first number "))
n = int(input("Give me the second number "))

my_list = []

def matrix(first_number,second_number):
    for i in range(first_number):
        list2 = []                   #this is a list that I created in order to store temporarily the numbers that are going to be generated in the second loop
        for j in range(second_number):
            list2.append(i*j)     
        my_list.append(list2)        #through this apend I store the temporary list into my main list, which is basicaly the matrix   
    return my_list

matrix(m,n)
