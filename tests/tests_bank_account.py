import unittest, os

from src.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000, log_file="transactions_log.txt")

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove("transactions_log.txt")


    def _count_lines(self, filename):
        with open(filename, 'r') as file:
            return len(file.readlines())
        

    def test_deposit(self):
        new_balance = self.account.deposit(25)
        self.assertEqual(new_balance, 1025, "El balance no es igual")



    def test_withdraw(self):
        new_balance = self.account.withdraw(25)
        self.assertEqual(new_balance, 975, "El balance no es igual")

    def test_get_balance(self):
        new_balance = self.account.get_balance()
        self.assertEqual(new_balance, 1000, "El balance no es igual")


    def test_transaction_log(self):
        self.account.deposit(25)
        self.assertTrue(os.path.exists("transactions_log.txt"))

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(25)
        assert self._count_lines(self.account.log_file) == 2
        self.account.withdraw(25)
        assert self._count_lines(self.account.log_file) == 3





