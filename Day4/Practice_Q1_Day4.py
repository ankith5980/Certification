user_A = set()
user_B = set()

while True:
    print("\n-- Movie Recommendation --")
    print("1. Enter Movies for the users")
    print("2. Show Common watches")
    print("3. Movies Unique to user A")
    print("4. Movies for user A based on user B")
    print("5. Exit")

    choice = input("Please select an option :: ")

    if choice == "1":
        n = int(input("Enter the number of Movies :: "))
        for i in range(n):
            mov_a = input(f"Enter movie {i+1} for User A :: ")
            user_A.add(mov_a)
        print(f"{len(user_A)} movies have been added for User A!")

        for j in range(n):
            mov_b = input(f"Enter movie {j+1} for User B :: ")
            user_B.add(mov_b)
        print(f"{len(user_B)} movies have been added for User B!")

    elif choice == "2":
        if not user_A or not user_B:
            print("Data not found! Please enter movies first.")
        else:
            common = user_A & user_B
            print(f"A and B commonly watched: {common}")

    elif choice == "3":
        if not user_A:
            print("No data found for User A!")
        else:
            unique_a = user_A - user_B
            print("Movies unique to User A ::")
            print(unique_a)

    elif choice == "4":
        if not user_B:
            print("No data found for User B!")
        else:
            recc = user_B - user_A
            print("Recommendations for A based on B ::")
            print(recc)

    elif choice == "5":
        print("Exiting program !!")
        break

    else:
        print("Invalid input! Please enter a valid option.")
