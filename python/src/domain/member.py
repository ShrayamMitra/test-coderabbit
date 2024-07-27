class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def __str__(self):
        return f'{self.name} ({self.email})'
