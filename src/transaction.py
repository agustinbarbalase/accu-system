class Transaction:
    def __init__(self, movements):
        if not movements:
            raise Exception("A transaction must have at least one movement")

        balance = 0
        for movement in movements:
            balance = movement.sum_for_balance(balance)

        if balance != 0:
            raise Exception("The balance of the transaction is not zero")

        for movement in movements:
            movement.register_into_account()
