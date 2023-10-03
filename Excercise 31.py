dog_years = int(input("How many years does your dog live? "))

def calculator(years_of_a_dogs_life):
    if years_of_a_dogs_life <= 2:
        converted_years = years_of_a_dogs_life * 10.5
        print(f"The human years that the dog has been living are {converted_years}")
    else:
        converted_years = 2 * 10.5 + ((years_of_a_dogs_life-2) * 4)
        print(f"The human years that the dog has been licing are {converted_years}")

calculator(dog_years)