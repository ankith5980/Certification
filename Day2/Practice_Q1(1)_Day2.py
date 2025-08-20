subject_set = set()
while True:
    print("---A Set for Subjects---")
    print("1. Add Subject")
    print("\n2. Remove Subject")
    print("\n3.Display All Subjects")
    print("\n4. Number of Unique Subjects")
    print("\n5. Exit")

    choice = input("Enter your choice :: ")

    if choice == "1":
        subject = input("Enter a subject :: ")
        subject_set.add(subject)
        print(f"Subject {subject} has been added !")

    elif choice == "2":
        subject = input("Enter a subject :: ")
        remove = subject_set.discard(subject)
        if remove is None:
            print(f"Subject {subject} has been removed !")
        else:
            print(f"Subject {subject} not found !")

    elif choice == "3":
        if subject_set:
            print("Subjects in the set are :: ")
            for subject in subject_set:
                print(f"{subject}")
        else:
            print("No subjects found !")

    elif choice == "4":
        print(f"The number of unique subjects are :: {len(subject_set)}")

    elif choice == "5":
        print("Exiting the program !")
        break

    else:
        print("Invalid choice. Please try again.")