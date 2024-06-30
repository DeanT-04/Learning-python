# Class to handle the display and user interaction
class display_pannel:
    def __init__(self, libary):
        self.libary = libary
        self.show_menu()

    # Method to display the menu and handle user choices
    def show_menu(self):
        while True:
            print("1.Add book\n2.Remove book\n3.Display all books\n4.Exit")
            self.libary.choice = int(input("Enter your choice:"))

            # Execute the corresponding method based on user's choice
            if self.libary.choice == 1:
                self.libary.add_book()
            elif self.libary.choice == 2:
                self.libary.remove_book()
            elif self.libary.choice == 3:
                self.libary.display_books()
            else:
                exit()

# Class to represent a book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to display book information
    def display_info(self):
        print(f"Title: {self.title} Author: {self.author}")

# Class to manage the library
class Libary:
    def __init__(self):
        self.books = []

    # Method to add a new book to the library
    def add_book(self):
        while True:
            title = input("Enter the title of the book (Type 'Finish' to exit):").upper()
            if title == 'FINISH':
                return
            author = input("Enter the author of the book:").upper()
            self.books.append(Book(title, author))
            print("Book added successfully")

    # Method to remove a book from the library
    def remove_book(self):
        title = input("Enter the title of the book to remove:").upper()
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    # Method to display all books in the library
    def display_books(self):
        for book in self.books:
            book.display_info()

# Create a library instance and start the display panel
libary = Libary()
display_pannel(libary)