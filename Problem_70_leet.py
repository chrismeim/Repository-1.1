n = int(input("give me the number of steps "))

list1 = []
for i in range(1,n+1):      #I append all the numbers from 1 to n into list1, this will later on be used as the "index"
    list1.append(i)

print(list1)

list2 = []                  #in list 3 I will append the number of combinations for each item of list1, the last item in list2 will also be the number of ways to arrange the steps for n stairs
list3 = []                  #list 3 performs only as a memory 
j = 0
for i in range(len(list1)):
    if i < 3:
        list2.append(1+j)
        list3.append(1+j)
        j += 1
    else:
        list2.append(list3[i-1]+list3[i-2])
        list3.append(list2[-1])

print(list2)

print(f"The number of ways is {list2[-1]}")