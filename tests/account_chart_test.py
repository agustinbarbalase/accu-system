import sys
import os
import unittest

from src.account import Account
from src.account_chart import AccountChart

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AccountChartTest(unittest.TestCase):

    def test01_a_recent_created_account_chart_is_empty(self):
        account_chart = AccountChart()
        self.assertEqual([], account_chart.list_accounts())

    def test02_add_account_to_account_chart(self):
        account_chart = AccountChart()
        account = Account()
        account_chart.add_account(account)

        self.assertEqual([account], account_chart.list_accounts())

    def test03_can_check_for_accounts_correctly(self):
        register_account = Account()
        unregister_account = Account()

        account_chart = AccountChart()
        account_chart.add_account(register_account)

        self.assertTrue(account_chart.has_account(register_account))
        self.assertFalse(account_chart.has_account(unregister_account))
