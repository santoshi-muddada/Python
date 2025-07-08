class BankAccount():
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance


class Deposit(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deposit(self, depositing):
        new_balance = self.get_balance() + depositing
        print(f"Account Number: {self.get_account_number()}")
        print(f"Current Balance: {self.get_balance()}")
        print(f"Depositing: {depositing}")
        print(f"New Balance after Deposit: {new_balance}")


class Withdrawing(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdrawing(self, withdrawing_amount):
        if withdrawing_amount <= self.get_balance():
            new_balance = self.get_balance() - withdrawing_amount
            print(f"Account Number: {self.get_account_number()}")
            print(f"Current Balance: {self.get_balance()}")
            print(f"Withdrawing: {withdrawing_amount}")
            print(f"New Balance after Withdrawal: {new_balance}")
        else:
            print("Insufficient funds! Withdrawal failed.")


# Creating objects and testing
deposit_obj = Deposit(12345678, 5000)
deposit_obj.deposit(7000)

withdraw_obj = Withdrawing(56743567, 4000)
withdraw_obj.withdrawing(3000)