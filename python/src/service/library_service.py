from domain.book import Book
from domain.member import Member
from persistence.book_repository import BookRepository
from persistence.member_repository import MemberRepository

class LibraryService:
    def __init__(self, book_repo, member_repo):
        self.book_repo = book_repo
        self.member_repo = member_repo

    def add_book(self, book_id, title, author, year):
        book = Book(book_id, title, author, year)
        self.book_repo.add_book(book)

    def add_member(self, member_id, name, email):
        member = Member(member_id, name, email)
        self.member_repo.add_member(member)

    def list_books(self):
        return self.book_repo.get_books()

    def list_members(self):
        return self.member_repo.get_members()
