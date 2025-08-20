fruits = set()

number = int(input("Enter the number of fruits :: "))

for i in range(number):
    fruit = input(f"Enter fruit {i+1} :: ")
    fruits.add(fruit)
    print(f"Fruit {fruit} has been added to the set !")

# Checking membership using user input
check = input("Enter a fruit to check :: ")
if check in fruits : 
    print(f"Yes, {check} is available !")
else:
    print(f"Sorry,  {check} is not available !")