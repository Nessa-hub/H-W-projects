acct1 = {"first_name":"Nii", "last_name":"Okai", "account_type":"current", "balance": 0.00}
acct2 = {"first_name":"Solomon", "last_name":"Oppong", "account_type":"savings", "balance": 10000.00}
old_balance1 = acct2.get("balance")
dict_bank_accounts = {"0001":acct1, "0002":acct2}

def deposit(bank_account,amount):
    new_balance1 = old_balance1 + amount
    print(new_balance1)
    acct2u = {"balance":new_balance1}
    acct2.update(acct2u)
    return new_balance1


deposit(acct2, 500)



print(dict_bank_accounts)


old_balance2 = acct2.get("balance")

def withdraw(bank_account,amount):
    new_balance2 = old_balance2 - amount
    print(new_balance2)
    return new_balance2

withdraw(acct2, 500)
