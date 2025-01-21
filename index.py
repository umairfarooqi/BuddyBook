# Welcome Message and Menu
print("\nWelcome to Bookify - Your Personal Library Manager!\n")

# Store books
library = []

while True:
    print("Choose an option from the menu below:\n ➜ 1. Add a New Book\n ➜ 2. View All Books\n ➜ 3. Exit\n ➜ 4. Delete a Book\n")

    # Ask the user to choose an option
    choice = input("Enter your choice (1/2/3/4): ")

    # Display the user's choice
    print("\nYou chose option: ", choice, "\n")

    # Handle the user's choice
    if choice == "1":
        print("Adding a new book.")

        # Ask the user for book details
        book_title = input("Enter Book title: ")
        book_author = input("Enter Book Author: ")

        new_book = {
            "title": book_title.upper(),
            "author": book_author.upper()
        }

        # Add the book to the library
        library.append(new_book)

        print("\nThe book is added\n")

    elif choice == "2":
        print("Viewing all books.\n")

        # Check if the library is empty
        if len(library) == 0:
            print("Your library is currently empty.\n")
        else:
            print("Here are the books in your library: \n")
            i = 0
            while i < len(library):
                book = library[i]
                print("Title: ", book["title"])
                print("Author: ", book["author"])
                i = i + 1

    elif choice == "3":
        print("Thanks have a good day!\n")
        break

    elif choice == "4":
        print("Deleting a book.\n")

        # Check if the library is empty
        if len(library) == 0:
            print("Your library is currently empty. No books to delete.\n")
        else:
            i = 0
            while i < len(library):
                book = library[i]
                print(i + 1, ". Title: ", book["title"], " Author: ", book["author"])
                i = i + 1

            # Ask the user for the book number to delete
            book_number = int(input("\nEnter the number of the book you want to delete: "))

            if 1 <= book_number <= len(library):
                book_number = book_number - 1
                library.pop(book_number)
                print("Deleted successfully")
            else:
                print("Book not found\n")
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.\n")