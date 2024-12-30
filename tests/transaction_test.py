import sys
import os
import unittest

from src.account import Account
from src.movement import Debit, Credit
from src.transaction import Transaction

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TransactionTest(unittest.TestCase):

    def test01_cannot_create_transaction_without_movements(self):
        with self.assertRaises(Exception) as ctx:
            Transaction([])
        self.assertEqual(
            "A transaction must have at least one movement", str(ctx.exception)
        )

    def test02_cannot_create_transaction_that_balance_arent_equal_in_two_sides(self):
        account = Account()

        with self.assertRaises(Exception) as ctx:
            Transaction(
                [
                    Debit.created_movement(100, account),
                    Debit.created_movement(100, account),
                ]
            )

        self.assertEqual(
            "The balance of the transaction is not zero", str(ctx.exception)
        )
        self.assertEqual(0, account.calculate_balance())

    def test03_a_valid_transaction_should_change_the_balance_of_accounts(self):
        account_one = Account()
        account_two = Account()

        transaction = Transaction(
            [
                Debit.created_movement(100, account_one),
                Credit.created_movement(100, account_two),
            ]
        )

        self.assertEqual(100, account_one.calculate_balance())
        self.assertEqual(-100, account_two.calculate_balance())
