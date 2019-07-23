class Account:
    def __init__(self,balance,account_name,pin,max_withdrawal,acc_type)#transactions)
       self.balance = balance
       self.account_name = account_name
       self.pin = pin
       self.max_withdrawal = max_withdrawal
       self.acc_type = acc_type
       #self.transactions = {}

    def withdraw(self)
       amount_to_withdraw = int(input("Enter the amount:" ))
       if amount_to_withdraw < max_withdrawal
          if amount_to_withdraw < balance
             balance = balance - amount_to_withdraw
             return balance

    def check_balance(self)
        print("Your current balance is {}".format(self.balance))

    def check_pin(self)
        print("Your pin is {}".format(self.pin))

    def deposit(self)
        deposit_amount = int(input("Enter the amount to deposit:" ))
        balance += deposit_amount
        print("Your new balance is:".format(self.balance))
