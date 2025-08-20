hobbies_A = set()
hobbies_B = set()

while True:
    print("---A set for hobbies of person A and B\n")
    print("1. Add Hobby for person A ::\n")
    print("2. Add Hobby for person B ::\n")
    print("3. Hobbies unique to person A ::\n")
    print("4. Hobbies unique to person B ::\n")
    print("5. Hobby(s) common to A and B ::\n")
    print("6. Set of All Hobbies ::\n")
    print("7. Exit\n")

    choice = input("Enter your choice :: ")

    if choice == "1":
        hobby_a = input("Enter a hobby for person A :: ")
        hobbies_A.add(hobby_a)
        print(f"Hobby {hobby_a} has been added for person A")

    elif choice == "2":
        hobby_b = input("Enter a hobby for person B :: ")
        hobbies_B.add(hobby_b)
        print(f"Hobby {hobby_b} has been added for person B")

    elif choice == "3":
        unique_A = hobbies_A - hobbies_B
        print(f"Hobbies unique to person A :: {unique_A}")

    elif choice == "4":
        unique_B = hobbies_B - hobbies_A
        print(f"Hobbies unique to person B :: {unique_B}")

    elif choice == "5":
        common = hobbies_A & hobbies_B
        print(f"Hobbies common to A and B :: {common}")

    elif choice == "6":
        all_hobbies = hobbies_A | hobbies_B
        print(f"Set of all Hobbies :: {all_hobbies}")

    elif choice == "7":
        print("Exiting the program !!")
        break
    else:
        print("Invalid choice. Please try again.")