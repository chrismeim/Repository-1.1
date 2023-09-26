x = [1,2,3,4,5,6,7,8,9,0,1,12,1,22,1,221]
even = 0
odd = 0

for i in range(len(x)):
    if x[i]%2 ==0:
        even +=1
    else:
        odd +=1

print(even, odd)
