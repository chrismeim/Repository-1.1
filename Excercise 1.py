numbers = []
k = 0
for i in range(1500, 2701, 5):
    if i%7 == 0:
        k +=1
        numbers.append(i)

print(f"The numbers that I have counted are {k}")
print(numbers)
