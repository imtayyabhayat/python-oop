from .publications import Publication

class Books(Publication):
    def __init__(self, authors, title, year, isbn):
        super().__init__(authors, title, year)
        self.authors = authors
        self.title = title
        self.year = year
        self.isbn = isbn
    
    def book(self):
        return f"{super().title()}\n{super().author()}\n{super().year()}\nISBN: {self.isbn}"
        
    def display(self):
        return self.book()
