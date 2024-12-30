class Movement:
    @classmethod
    def register_movement(cls, value, account):
        if value < 0:
            raise Exception("The value must be positive")

        new_movement = cls(value, account)
        new_movement.register_into_account()

        return new_movement

    @classmethod
    def created_movement(cls, value, account):
        if value < 0:
            raise Exception("The value must be positive")

        return cls(value, account)

    def __init__(self, value, account):
        self.value = value
        self.account = account

    def register_into_account(self):
        self.account.add_register(self)

    def is_for(self, value):
        return self.value == value


class Debit(Movement):
    def sum_for_balance(self, balance):
        return balance + self.value

    def accept(self, visitor):
        visitor.visit_debit(self)


class Credit(Movement):
    def sum_for_balance(self, balance):
        return balance - self.value

    def accept(self, visitor):
        visitor.visit_credit(self)
