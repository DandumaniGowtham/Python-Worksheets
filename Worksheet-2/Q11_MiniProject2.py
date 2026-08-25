class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "name": book_name,
            "author": author,
            "available": True
        }

        self.books.append(book)
        print("Book added successfully.")

    def issue_book(self):
        book_id = int(input("Enter Book id to issue: "))

        for book in self.books:
            if book["id"] == book_id:
                if book["available"]:
                    book["available"] = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book does not exist.")

    def return_book(self):
        book_id = int(input("Enter Book ID to return: "))

        for book in self.books:
            if book["id"] == book_id:
                book["available"] = True
                print("Book returned successfully.")
                return

        print("Book not found.")

    def display_available_books(self):
        print("\nAvailable Books:")

        found = False
        for book in self.books:
            if book["available"]:
                print("ID:", book["id"])
                print("Name:", book["name"])
                print("Author:", book["author"])
                print()
                found = True

        if not found:
            print("No books available.")

library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Available Books")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.issue_book()

    elif choice == 3:
        library.return_book()

    elif choice == 4:
        library.display_available_books()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")