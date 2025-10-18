class BankAccount:

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder=account_holder
        self.balance=initial_balance

    def deposit(self,amount):
        
        if amount>0:
            self.balance+=float(amount)
        else:   
            raise ValueError ("Withdrawal amount must be positive.")  
        return self.balance
    
    def withdraw(self, amount):

        if amount>0 and amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            raise Exception("Insufficient funds.")
        

    def get_balance(self):
        return self.balance
    
    def get_account_holder(self):
        return self.account_holder