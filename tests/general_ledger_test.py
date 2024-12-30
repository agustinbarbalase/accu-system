import sys
import os
import unittest

from src.account import Account
from src.movement import Debit, Credit
from src.general_ledger import GeneralLedger

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class GeneralLedgerTest(unittest.TestCase):

    def test01_create_general_ledger(self):
        general_ledger = GeneralLedger.generate_for(None)
        self.assertEqual([], general_ledger)

    def test02_an_account_with_debit_generate_general_ledger(self):
        account_one = Account()
        debit_side = Debit.register_movement(100, account_one)

        general_ledger = GeneralLedger.generate_for(account_one)
        self.assertEqual(1, len(general_ledger))
        self.assertEqual("Debit for 100", general_ledger[0])

    def test03_an_account_with_credit_generate_general_ledger(self):
        account_one = Account()
        credit_side = Credit.register_movement(100, account_one)

        general_ledger = GeneralLedger.generate_for(account_one)
        self.assertEqual(1, len(general_ledger))
        self.assertEqual("Credit for 100", general_ledger[0])
