from persistence.database import Database

class BookRepository:
    def __init__(self, database):
        self.database = database

    def add_book(self, book):
        self.database.add_book(book)

    def get_books(self):
        return self.database.get_books()
