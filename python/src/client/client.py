from persistence.database import Database
from persistence.book_repository import BookRepository
from persistence.member_repository import MemberRepository
from service.library_service import LibraryService

# Initialize the database and repositories
database = Database()
book_repo = BookRepository(database)
member_repo = MemberRepository(database)
library_service = LibraryService(book_repo, member_repo)

# Add some books and members
library_service.add_book(1, '1984', 'George Orwell', 1949)
library_service.add_book(2, 'To Kill a Mockingbird', 'Harper Lee', 1960)

library_service.add_member(1, 'John Doe', 'john@example.com')
library_service.add_member(2, 'Jane Smith', 'jane@example.com')

# List books and members
print("Books in the library:")
for book in library_service.list_books():
    print(book)

print("\nMembers in the library:")
for member in library_service.list_members():
    print(member)
