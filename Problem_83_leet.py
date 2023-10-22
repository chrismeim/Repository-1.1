
list1 = [1,2,3,1,2,1,2,3,4,4,4,5,6,6,1]

i = 0 
while i <len(list1):
    j = 0
    while j <len(list1):
        if list1[i] == list1[j] and i!=j:
            list1.pop(j)
        else: 
            j +=1
    i +=1

print(list1)

