library = []

def addDetails():  # CHOICE 1
    n = int(input("Enter the number of records :: "))

    for i in range(n):
        print(f"\nEnter the details of book {i+1}")
        book_id = input("Enter book ID :: ")
        book_name = input("Enter book name :: ")
        author_name = input("Enter author name :: ")
        publishing_year = input("Enter year of publication :: ")

        book = (book_id, book_name, author_name, publishing_year)
        library.append(book)

    print(f"\n✅ {n} book(s) added successfully!")


def displayBooks():  # CHOICE 2
    if not library:
        print("No Records Found !! ")
    else:
        print("\nBooks Currently Available:")
        for book in library:
            print(f"BookID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")


def removeBooks():  # CHOICE 3
    if not library:
        print("No Data Available")
    else:
        book_id = input("Enter the Book ID you want to remove :: ")
        for book in library:
            if book[0] == book_id:
                library.remove(book)
                print(f"✅ Book with ID {book_id} removed successfully!")
                return
        print("❌ Book not found!")


def searchById():  # CHOICE 4
    book_id = input("Enter the Book ID to search :: ")
    for book in library:
        if book[0] == book_id:
            print(f"\n✅ Book Found: BookID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
            return
    print("❌ Book not found!")


def searchByTitle():  # CHOICE 5
    title = input("Enter the Book Title to search :: ").lower()
    found = False
    for book in library:
        if book[1].lower() == title:
            print(f"\n✅ Book Found: BookID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
            found = True
    if not found:
        print("❌ Book not found!")


def booksBeforeYear():  # CHOICE 6
    year = int(input("Enter the year :: "))
    found = False
    print(f"\nBooks published before {year}:")
    for book in library:
        if int(book[3]) < year:
            print(f"BookID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
            found = True
    if not found:
        print("❌ No books found before this year!")


def bookCount():  # CHOICE 7
    if not library:
        print("No Data Available")
        return
    count_dict = {}
    for book in library:
        author = book[2]
        count_dict[author] = count_dict.get(author, 0) + 1

    print("\nBook Count per Author:")
    for author, count in count_dict.items():
        print(f"{author}: {count} book(s)")


# Main Menu
while True:
    print("\n--Library Book Tracker--")
    print("1. Add Details")
    print("2. Display Books")
    print("3. Remove Record")
    print("4. Search Book By Id")
    print("5. Search Book by Title")
    print("6. Books before a specific year")
    print("7. Book count for each author")
    print("8. Exit")

    choice = input("Enter your choice :: ")

    if choice == "1":
        addDetails()
    elif choice == "2":
        displayBooks()
    elif choice == "3":
        removeBooks()
    elif choice == "4":
        searchById()
    elif choice == "5":
        searchByTitle()
    elif choice == "6":
        booksBeforeYear()
    elif choice == "7":
        bookCount()
    elif choice == "8":
        print("Exiting Program !! .. See ya later 👋\n")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
