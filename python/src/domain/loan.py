class Loan:
    def __init__(self, loan_id, book, member, due_date):
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.due_date = due_date

    def __str__(self):
        return f'Loan {self.loan_id}: {self.book.title} to {self.member.name}, due {self.due_date}'
