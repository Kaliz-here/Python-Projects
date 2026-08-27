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

        if(available == True):
            print(True)
        else:
            self.available = available
            
        self.borrower_name = borrower_name

    def borrow_book(borrower_name):
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
    title = input("\nEnter Title : ")
    author = input("Enter author name : ")
    isbn = input("Enter ISBN : ")
    available = True
    borrower_name = None

    library_book = LibrarySystem(title, author, isbn, available, borrower_name)
    book_list.append(library_book)

    start += 1

for i in book_list:
    print(i)