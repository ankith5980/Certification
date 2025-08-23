items = ["milk", "bread", "egg", "apple", "butter"]
prices = [40, 25, 5, 30, 55]

total_bill = 0.0
shopping_list = "" 

print("--- Welcome to the Store ---")
print("Type 'done' when you are finished.")
print("-" * 28)



while True:

    print(f"Available items: {', '.join(items)}")
    

    item_bought = input("What would you like to buy? ").lower()


    if item_bought == 'done':
        break 


    if item_bought in items:

        item_index = items.index(item_bought)
        

        price = prices[item_index]


        try:
            quantity = int(input(f"How many units of {item_bought}?: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.\n")
            continue 

        cost = price * quantity
        total_bill += cost
        

        shopping_list += f"- {item_bought.capitalize()} (x{quantity}): ₹{cost:.2f}\n"

        print(f"Added {quantity} x {item_bought}. Current total is ₹{total_bill:.2f}\n")
    else:
        print("Sorry, that item is not available. Please try again.\n")


print("\n" + "=" * 28)
print("         FINAL BILL")
print("=" * 28)

if total_bill > 0:
    print("Items Purchased:\n" + shopping_list)
    print(f"Sub-Total: ₹{total_bill:.2f}")

    final_bill = total_bill
    if total_bill > 1000:
        discount = total_bill * 0.20  # 20% discount
        final_bill = total_bill - discount
        print(f"Discount (20%): -₹{discount:.2f}")
    elif total_bill > 500:
        discount = total_bill * 0.10  # 10% discount
        final_bill = total_bill - discount
        print(f"Discount (10%): -₹{discount:.2f}")

    print("-" * 28)
    print(f"TOTAL TO PAY: ₹{final_bill:.2f}")
else:
    print("You did not purchase anything.")

print("\nThank you for shopping!")