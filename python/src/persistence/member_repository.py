from persistence.database import Database

class MemberRepository:
    def __init__(self, database):
        self.database = database

    def add_member(self, member):
        self.database.add_member(member)

    def get_members(self):
        return self.database.get_members()
