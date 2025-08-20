# Shopping Cart System using Python lists

def main():
    cart = []
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Cart")
        print("5. Search Item")
        print("6. Slice Cart")
        print("7. Sort Cart")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            item = input("Enter item to add: ")
            cart.append(item)
            print(f"Added '{item}' to cart.")

        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in cart:
                cart.remove(item)
                print(f"Removed '{item}' from cart.")
            else:
                print(f"'{item}' not found in cart.")

        elif choice == '3':
            old_item = input("Enter item to update: ")
            if old_item in cart:
                new_item = input("Enter new item: ")
                idx = cart.index(old_item)
                cart[idx] = new_item
                print(f"Updated '{old_item}' to '{new_item}'.")
            else:
                print(f"'{old_item}' not found in cart.")

        elif choice == '4':
            if cart:
                print("\nItems in Cart:")
                for idx, item in enumerate(cart):
                    print(f"Position {idx}: {item}")
            else:
                print("Cart is empty.")

        elif choice == '5':
            item = input("Enter item to search: ")
            if item in cart:
                print(f"'{item}' found at position {cart.index(item)}.")
            else:
                print(f"'{item}' not found in cart.")

        elif choice == '6':
            if cart:
                start = input("Enter start index: ")
                end = input("Enter end index: ")
                try:
                    start = int(start)
                    end = int(end)
                    print(f"Cart slice [{start}:{end}]: {cart[start:end]}")
                except ValueError:
                    print("Invalid index values.")
            else:
                print("Cart is empty.")

        elif choice == '7':
            cart.sort()
            print("Cart sorted alphabetically.")
            print(cart)

        elif choice == '8':
            print("Exiting Shopping Cart System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()