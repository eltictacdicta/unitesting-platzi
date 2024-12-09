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
        assert self.account.deposit(25) == 1025


    def test_withdraw(self):
        assert self.account.withdraw(25) == 975

    def test_get_balance(self):
        assert self.account.get_balance() == 1000

    def test_transaction_log(self):

        new_balance = self.account.deposit(25)
        os.path.exists("transactions_log.txt")
        with open("transactions_log.txt", "r") as file:
            log_content = file.read()
        assert f"Deposited: 25, New Balance: {new_balance}" in log_content

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(25)
        assert self._count_lines(self.account.log_file) == 2
        self.account.withdraw(25)
        assert self._count_lines(self.account.log_file) == 3





