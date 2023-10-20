number = [1,2,3, 4]

x = 0

for i in range(len(number)):
    if i != len(number):
        x += number[i]*10**(len(number)-i-1)
    else:
        x += number[i]

x += 1

new_list = []
x = str(x)
for i in range(len(x)):
    new_list.append(x[i])

print(new_list)