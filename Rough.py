class Library():
    def __init__(self):
        self.books = []

    def addbook(self):
        book_id = int(input("Enter book id: "))
        book_name = input("Enter book name: ")
        author_name = input("Enter Author name: ")

        book = {
            "id" : book_id,
            "name" : book_name,
            "author name" : author_name,
            "available" : True
        }  
        self.books.append(book)

    def issue_book(self):
        book_id = int(input("Enter book id: "))

        for book in self.books:
            if book["id"] == book_id:
                if book["available"]:
                    print("book issued Successfully")
                    book["available"] = False
                else:
                    print("Book is already issued")
                return
        else:
            print("Book not found")

    def return_book(self):
        book_id = int(input("Enter book id: "))
        for book in self.books:
            if book["id"] == book_id:
                book["available"] = True
                print("Book returned successfully")
                return
            
        print("Invalid book id")


    