import sys
import os
import unittest

from src.account import Account
from src.movement import Debit, Credit

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test01_when_create_account_the_balance_should_be_zero(self):
        self.assertEqual(0, self.account.calculate_balance())

    def test02_when_debit_the_balance_change(self):
        Debit.register_movement(100, self.account)

        self.assertEqual(100, self.account.calculate_balance())

    def test03_when_debit_multiple_times_the_balance_change_correctly(self):
        Debit.register_movement(100, self.account)
        Debit.register_movement(100, self.account)

        self.assertEqual(200, self.account.calculate_balance())

    def test04_when_credit_the_balance_change_correctly(self):
        Credit.register_movement(100, self.account)

        self.assertEqual(-100, self.account.calculate_balance())

    def test05_account_should_has_register_transactions(self):
        registered_debit = Debit.register_movement(100, self.account)
        unregistered_debit = Debit.created_movement(100, self.account)

        self.assertTrue(self.account.has_register(registered_debit))
        self.assertFalse(self.account.has_register(unregistered_debit))
