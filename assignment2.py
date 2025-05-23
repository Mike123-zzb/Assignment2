import math

people = int(input("Enter the number of people attending the cookout: "))
hot_dogs_per_person = int(input("Enter the number of hot dogs each person will get: "))

HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

total_hot_dogs = people * hot_dogs_per_person
hot_dog_packages = math.ceil(total_hot_dogs / HOT_DOGS_PER_PACKAGE)
bun_packages = math.ceil(total_hot_dogs / BUNS_PER_PACKAGE)

leftover_hot_dogs = (hot_dog_packages * HOT_DOGS_PER_PACKAGE) - total_hot_dogs
leftover_buns = (bun_packages * BUNS_PER_PACKAGE) - total_hot_dogs

print("\nMinimum number of hot dog packages needed:", hot_dog_packages)
print("Minimum number of hot dog bun packages needed:", bun_packages)
print("Hot dogs left over:", leftover_hot_dogs)
print("Hot dog buns left over:", leftover_buns)
