# Create a class named Library
# Create constructor method to open a txt file in a+ mode
class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = open(
            self.file_name, "a+"
        )  # a+ mode allows to read and write to the file

    # Create a method to write to the file
    def write(self, text):
        self.file.write(text + "\n")

    # Create a method to read from the file
    def read(self):
        self.file.seek(0)
        return self.file.read()

    # Create a method to close the file
    def close(self):
        self.file.close()

    # Create a destructor method to close the file
    def __del__(self):
        self.file.close()
        print("File closed \n")

    # Create method to list books in the file
    # If the file is empty, print "No books found"
    # Use splitlines to split the books into a list
    def list_books(self):
        books = self.read()
        if not books:
            print("No books found \n")
            return
        books = books.split("\n")
        for book in books:
            print(book)

    # Create method to add book to the file (title, author, release year, number of pages)
    # Each book will be on a new line
    # Separate title, author, release year, and number of pages with a comma
    def add_book(self, title, author, release_year, num_pages):
        book = f"{title}, {author}, {release_year}, {num_pages}"
        self.write(book)
        print("Book added \n")

    # Create method to remove book from the file
    # Title is the first item in the book string split by a comma (case insensitive)
    # If the title is not found in the file, print "Book not found" and return to the menu
    # If the title is the same as the title in the book string, remove the book from the file and delete the empty line
    def remove_book(self, title):
        books = self.read()
        books = books.split("\n")
        for book in books:
            if book.split(",")[0].strip().lower() == title.lower():
                books.remove(book)
                self.file.seek(0)
                self.file.truncate()
                for book in books:
                    if book:
                        self.write(book)
                print("Book removed \n")
                return
        print("Book not found \n")


# Create an instance of the Library class named lib
lib = Library("books.txt")


# Create a menu to interact with the library
def menu():
    print("1. List books")
    print("2. Add book")
    print("3. Remove book")
    print("Q. Exit")
    choice = input("Choose an option: ")
    return choice


# On program start, display the menu
menu_choice = menu()

# While the user does not choose to exit, continue to display the menu
while menu_choice != "q" and menu_choice != "Q":
    if menu_choice == "1":
        lib.list_books()
    elif menu_choice == "2":
        title = input("Enter title: ")
        author = input("Enter author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        lib.add_book(title, author, release_year, num_pages)
    elif menu_choice == "3":
        title = input("Enter title: ")
        lib.remove_book(title)
    menu_choice = menu()

lib.close()
