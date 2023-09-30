result = ""
for i in range(0,7):    #number of rows
    for j in range(0,7):  #number of columns
        if (((j == 1 or j == 5) and i != 0) or ((i ==0 or i ==3) and (j >1 and j <5))):
            result = result + "*" 
        else:
            result = result + " "
    result = result + "\n"
            
print(result)