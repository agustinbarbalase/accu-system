class Account:

    def __init__(self):
        self.transaction_sides = []

    def add_register(self, transaction_side):
        self.transaction_sides.append(transaction_side)

    def calculate_balance(self):
        balance = 0
        for transaction_side in self.transaction_sides:
            balance = transaction_side.sum_for_balance(balance)
        return balance

    def has_register(self, transaction_side):
        return transaction_side in self.transaction_sides

    def do_for_transaction(self, closure):
        for transaction_side in self.transaction_sides:
            closure(transaction_side)
