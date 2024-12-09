class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        # Log the creation of the account.
        self._log_transaction("Cuenta creada")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited: {amount}, New Balance: {self.balance}")
        else:
            raise ValueError("El monto del depósito debe ser mayor que cero.")
        return self.balance
    
    def _log_transaction(self,message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrawn: {amount}, New Balance: {self.balance}")
        return self.balance

    def get_balance(self):
        return self.balance
