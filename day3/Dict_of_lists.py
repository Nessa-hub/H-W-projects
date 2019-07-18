acct1 = ["Nii", "Okai", "current", 0.00]
acct2 = ["Solomon", "Oppong", "savings", 10000.00]
dict_of_lists = {"0001":acct1, "0002":acct2}

print(dict_of_lists)

old_balance1 = acct2.pop(3)

def deposit(bank_account,amount):
    new_balance1 = old_balance1 + amount
    print(new_balance1)
    acct2.append(new_balance1)
    print(dict_of_lists)
    return new_balance1

deposit(acct2, 500)

old_balance2 = acct2.pop(3)

def withdraw(bank_account,amount):
     new_balance2 = old_balance2 - amount
     print(new_balance2)
     acct2.append(new_balance2)
     print(dict_of_lists)
     return new_balance2

withdraw(acct2, 500)
