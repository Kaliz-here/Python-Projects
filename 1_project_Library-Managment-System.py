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
        if(isbn != ""):
            raise ValueError("ISBN must me uniqu..!")
        else:
            self.isbn = isbn

        self.available = available
        self.borrower_name = borrower_name