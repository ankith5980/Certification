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
        try:
            price = float(input("Enter price: "))
            cart.append({"name": item, "price": price})
            print(f"Added {item} with price {price}.")
        except ValueError:
            print("Invalid price. Item not added.")

    elif choice == '2':
        item = input("Enter item to remove: ")
        for product in cart:
            if product["name"] == item:
                cart.remove(product)
                print(f"Removed {item} from cart.")
                break
        else:
            print(f"{item} not found in cart.")

    elif choice == '3':
        old_item = input("Enter item to update: ")
        for product in cart:
            if product["name"] == old_item:
                new_item = input("Enter new item name: ")
                try:
                    new_price = float(input("Enter new price: "))
                    product["name"] = new_item
                    product["price"] = new_price
                    print(f"Updated {old_item} to {new_item} with price {new_price}.")
                except ValueError:
                    print("Invalid price. Update failed.")
                break
        else:
            print(f"{old_item} not found in cart.")

    elif choice == '4':
        if cart:
            print("\nItems in Cart:")
            total = 0
            for idx, product in enumerate(cart):
                name, price = product["name"], product["price"]
                # Apply discount
                if price >= 500:
                    discount = 0.10
                else:
                    discount = 0.15
                discounted_price = price - (price * discount)
                total += discounted_price
                print(f"Position {idx}: {name} | Original: {price} | Discount: {int(discount*100)}% | Final: {discounted_price:.2f}")
            print(f"\nTotal Price after discount: {total:.2f}")
        else:
            print("Cart is empty.")

    elif choice == '5':
        item = input("Enter item to search: ")
        for idx, product in enumerate(cart):
            if product["name"] == item:
                print(f"{item} found at position {idx} with price {product['price']}")
                break
        else:
            print(f"{item} not found in cart.")

    elif choice == '6':
        if cart:
            start = input("Enter start index: ")
            end = input("Enter end index: ")
            try:
                start, end = int(start), int(end)
                print("Cart slice:")
                for idx, product in enumerate(cart[start:end], start):
                    print(f"Position {idx}: {product['name']} | Price: {product['price']}")
            except ValueError:
                print("Invalid index values.")
        else:
            print("Cart is empty.")

    elif choice == '7':
        cart.sort()
        print("Cart sorted alphabetically by item name.")
        for product in cart:
            print(f"{product['name']} | Price: {product['price']}")

    elif choice == '8':
        print("Exiting Shopping Cart System.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
