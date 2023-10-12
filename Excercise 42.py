numbers = []
count = 1
number = int(input("Give me a number, if you want to stop please press 0"))
while number != 0:
    numbers.append(number)
    number = int(input("Give me a number, if you want to stop please press 0"))
    if number != 0:
        count += 1

sum_of_numbers = sum(numbers)
average_of_numbers = sum(numbers) / count

print(f"The sum of the numbers is {sum_of_numbers}")
print(f"The average of the numbers is {average_of_numbers}")