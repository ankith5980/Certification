books = set()

while True:
    print("\n--- Library Book Tracker Menu ---")
    print("1. Add Book")
    print("2. Remove Book (Issued)")
    print("3. Show All Available Books")
    print("4. Check Book Availability")
    print("5. Show Total Number of Books")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        book = input("Enter book name to add: ")
        books.add(book)
        print(f"Book '{book}' added to collection.")

    elif choice == '2':
        book = input("Enter book name to remove (issued): ")
        if book in books:
            books.remove(book)
            print(f"Book '{book}' removed from collection.")
        else:
            print(f"Book '{book}' not found in collection.")

    elif choice == '3':
        if books:
            print("\nAvailable Books:")
            for book in books:
                print(book)
        else:
            print("No books available in the collection.")

    elif choice == '4':
        book = input("Enter book name to check: ")
        if book in books:
            print(f"Book '{book}' is available.")
        else:
            print(f"Book '{book}' is not available.")

    elif choice == '5':
        print(f"Total number of books: {len(books)}")

    elif choice == '6':
        print("Exiting Library Book Tracker.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")