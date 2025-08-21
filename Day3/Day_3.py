cart = ["Apple", "Banana", "Cherry", "Dragon Fruit"]

# Printing first element in the list named cart
print(cart[0])

# Slicing in the elements in the list cart
sliced_1 = cart[1:3]
print(sliced_1)

# adding an element into the list using append function
cart.append("Orange")
print(cart)
cart.extend(["Mango", "Papaya", "Carrot"])
print(cart)

# Checking membership of a item in the list
find_fruit = input("Enter the fruit to be checked :: ")
if find_fruit in cart:
    print(f"Fruit {find_fruit} found in cart !")
else:
    print(f"Fruit {find_fruit} not found !")

# Removing element for a list using remove
cart.remove("Mango")
print(cart)

# Removing element for a list using pop
remove_2 = cart.pop()
print(remove_2)

