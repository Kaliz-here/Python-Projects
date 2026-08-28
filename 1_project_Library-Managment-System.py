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

print("Library Books")
for i in book_list:
    print(i)