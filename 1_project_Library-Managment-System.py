class LibrarySystem:
    def __init__(self, title, author, isbn, available=True, borrower_name=None):

        # check title validation
        if(title == ""):
            raise ValueError("\nInvalid Title..!")
        else:
            self.title = title

        # check author validation
        if(author == ""):
            raise ValueError("\nInvalid Author Name..!")
        else:
            self.author = author

        # check isbn number validation
        if(isbn == ""):
            raise ValueError("ISBN must me uniqu..!")
        else:
            self.isbn = isbn

        self.available = available   
        self.borrower_name = borrower_name

    def borrow_book(self, borrower_name):
        pass

    def return_book(self):
        pass

    def __str__(self):
        details = f"\n\nTitle : {self.title}\n"
        details += f"Author Name : {self.author}\n"
        details += f"ISBN : {self.isbn}\n"
        details += f"Status : {self.available}\n"
        details += f"Borrower Name : {self.borrower_name}\n"

        return details


book_list = []
book_dict = {}

start = 1


def employeeMenu():
    while True:
        print("""
                1. Search Book
                2. Add Book
                3. Remove Book
                4. Print All Books
                5. Total Books
                6. Available Book
                7. Exit
""")

        # Search book dict using ISBN
        employeeChoice = int(input("Enter choice : "))
        if(employeeChoice == 1):
            searchBook = input("Enter ISBN : ")
            if searchBook in book_dict:
                print(book_dict[searchBook])
                print("\nBook Found..!")

            else:
                print("Not Found..!")

        elif(employeeChoice == 2):
            pass

        elif(employeeChoice == 3):
            pass

        elif(employeeChoice == 4):
            pass

        elif(employeeChoice == 5):
            pass

        elif(employeeChoice == 6):
            pass

        elif(employeeChoice == 7):
            break

        else:
            print("Invalid Choice..!")

def customerMenu():
    while True:
        print("""
                1. Borrow Book
                2. Return Book
                3. Search Book
                4. View Available Books
                5. Exit
""")

        customerChoice = int("Enter Choice : ")

        if(customerChoice == 1):
            pass

        elif(customerChoice == 2):
            pass

        elif(customerChoice == 3):
            pass

        elif(customerChoice == 4):
            pass

        elif(customerChoice == 5):
            break

        else:
            print("Invalid Choice..!")

# add objects in list and dict until while loop get false
books = int(input("\nEnter Books > "))
while start <= books:

    print(f"\nBook >> {start}")
    title = input("Enter Title : ")
    author = input("Enter author name : ")
    isbn = input("Enter ISBN : ")

    if isbn in book_dict:
        print("ISBN alredy exist..!")
        print(f"\nBook >> {start} again..!")

        continue

    available = True
    borrower_name = None

    library_book = LibrarySystem(title, author, isbn, available, borrower_name)
    book_list.append(library_book) # Store books objects in list
    book_dict[isbn] = library_book # find object using ISBN

    start += 1

# create customer menu and employee menu
print("""
        1. Employee Menu
        2. Customer Menu
""")
userChoice = int(input("\nEnter Choice : "))
if(userChoice == 1):
    employeeMenu()

elif(userChoice == 2):
    customerMenu()

else:
    print("Invalid Choice..!")