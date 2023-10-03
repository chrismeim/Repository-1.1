result = ""

for i in range(0,6):    #number of rows
    for j in range(0,7):  #number of columns
        if ((i == 1 or i == 3 or i == 5) and ( j ==1 or j == 2 or j==3 or j ==4 or j == 5)) or ((i == 2 or i == 3 or i == 4 or i ==5) and j==1):
            result = result + "*" 
        else:
            result = result + " "
    result = result + "\n"

print(result)