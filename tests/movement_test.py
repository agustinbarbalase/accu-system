import sys
import os
import unittest

from src.movement import Debit, Credit

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MovementTest(unittest.TestCase):

    def test01_cannot_create_negative_debit_or_credit(self):
        with self.assertRaises(Exception) as ctx:
            Debit.created_movement(-100, None)
        self.assertEqual("The value must be positive", str(ctx.exception))

        with self.assertRaises(Exception) as ctx:
            Credit.created_movement(-100, None)
        self.assertEqual("The value must be positive", str(ctx.exception))

    def test02_movement_should_have_value(self):
        debit = Debit.created_movement(100, None)
        credit = Credit.created_movement(100, None)

        self.assertTrue(debit.is_for(100))
        self.assertTrue(credit.is_for(100))

    def test03_debit_sum_for_balance_correctly(self):
        debit = Debit.created_movement(100, None)
        self.assertEqual(100, debit.sum_for_balance(0))

    def test04_credit_sum_for_balance_correctly(self):
        credit = Credit.created_movement(100, None)
        self.assertEqual(-100, credit.sum_for_balance(0))
