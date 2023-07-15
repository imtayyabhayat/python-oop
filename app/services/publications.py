class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def title(self):
        return f"Title: {self.title}"
    
    def author(self):
        return f"Author: {self.author}"
    
    def year(self):
        return f"Year: {self.year}"