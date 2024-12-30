class GeneralLedger:
    @classmethod
    def generate_for(cls, account):
        if account is None:
            return []
        return cls(account).generate_report()

    def __init__(self, account):
        self.account = account
        self.summary = []

    def generate_report(self):
        def closure(transaction):
            transaction.accept(self)

        self.account.do_for_transaction(closure)
        return self.summary

    def visit_debit(self, debit):
        self.summary.append(f"Debit for {debit.value}")

    def visit_credit(self, credit):
        self.summary.append(f"Credit for {credit.value}")
