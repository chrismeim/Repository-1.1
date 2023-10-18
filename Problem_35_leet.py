list1 = [1,2,4,5]

target_value = int(input("give me the target value "))

dummy = True
for index, num in enumerate(list1):
    if num == target_value:
        print(f"the index is at {index}")
        dummy = False

if dummy == True:
    k = 0
    while k <= len(list1):
        if target_value > list1[k]:
            k += 1
        else:
            print(f"the index would be at {k}")
            break
    