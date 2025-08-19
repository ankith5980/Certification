# Design a Shopping Cart System using Python lists.
# Your program should:
# 1. Create an empty shopping cart using a list.
# 2. Provide a menu with the following options:
# Add Item → Add a new item to the cart.
# Remove Item → Remove an existing item from the cart.
# Update Item → Replace an existing item with a new one.
# View Cart → Display all items in the cart with their positions.
# Search Item → Check if an item exists in the cart and display its position.
# Slice Cart → Display a portion of the cart using start and end indexes.
# Sort Cart → Arrange all items alphabetically.
# Exit → Quit the program.
# 3. Use all possible list operations such as append(), remove(), insert(), sort(), slice, index(), len(), etc.

cart = [

]

# Add items to a list
cart.append("Apple")
cart.append("Orange")
cart.append("Banana")
print(cart)

# Remove items from the list
cart.remove("Orange")
print(cart)

# Update items in the list using index
cart[1] = "Grapes"
print(cart)

# view all the elements in the list using enumerate()
for index, item in enumerate(cart):
    print(f"Item {index}: {item}")

# Search items using the index function and in operator
item_to_search = "Grapes"
if item_to_search in cart:
    print(f"Found {item_to_search} at index {cart.index(item_to_search)}")
else:
    print(f"{item_to_search} not found in cart.")

# Slicing the list
print(cart[1:3])
print(cart[:2])

# Sorting the elements in the list
cart.sort()
print("Sorted cart:", cart)

# Check the length of the list
print("Total items in cart:", len(cart))

# Delete an item indirectly from the list by using remove
cart.remove("Apple")
print(cart)

# Total number of items
print("Total items in the cart after all operations:", len(cart))