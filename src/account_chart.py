class AccountChart:
    def __init__(self):
        self.accounts = []

    def list_accounts(self):
        return self.accounts

    def add_account(self, account):
        self.accounts.append(account)

    def has_account(self, account):
        return account in self.accounts
