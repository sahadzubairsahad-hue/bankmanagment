'''Python OOP â€“ Bank Account Management System
=============================================

Create a menu-driven Bank Account Management System using Object-Oriented Programming (OOP), List, and Dictionary in Python.

Requirements
------------

Create a class named `Bank`.

Inside the class, maintain all bank account details using a list of dictionaries.

Each account should contain:

```text
Account Number
Customer Name
Balance
```

Operations to Implement
------------------------
1. Create Account

Create a new bank account with:

* Account number
* Customer name
* Initial balance

Rules:

* Account number must be unique.
* Minimum initial balance should be **â‚¹500**.
* Display an appropriate message if the account already exists or the balance is insufficient.

2. Display All Accounts

Display the details of all existing accounts.

If there are no accounts, display:

```text
No accounts found.
```

3. Search Account

Ask the user for an account number and display the corresponding:

* Account number
* Customer name
* Balance

Display an appropriate message if the account does not exist.

4. Update Account

Ask for an account number and provide options to:

```text
1. Update Customer Name
2. Update Account Number
```

Rules:

* The new account number must not already exist.
* Display an appropriate message for an invalid account number.

5. Deposit Money

Ask for:

* Account number
* Deposit amount

Rules:

* Deposit amount must be greater than `0`.
* Update the account balance after a successful deposit.

6. Withdraw Money

Ask for:

* Account number
* Withdrawal amount

Rules:

* Withdrawal amount must be greater than `0`.
* After withdrawal, the account must maintain a minimum balance of **â‚¹500**.
* Display an appropriate message if the withdrawal is not allowed.

7. Delete Account

Ask for an account number and delete the corresponding account.

Rule:

An account can be deleted only when its balance is â‚¹0.

If the balance is not zero, display an appropriate message.

8. Exit

Exit the program when the user selects the exit option.

---

Expected Menu

```text
===== BANK MANAGEMENT SYSTEM =====

1. Create Account
2. Display Accounts
3. Search Account
4. Update Account
5. Deposit
6. Withdraw
7. Delete Account
8. Exit

Enter your choice:
```
'''

class Bank:
    def __init__(self):
        self.accounts=[]

    def create_account(self):
        account_no=int(input("enter the acc no:"))
        for acc in self.accounts:
            if acc["account_no"]==account_no:
                print("account already exist")
            
        name=input("enter the name:")
        balance=float(input("enter the balance:"))
        if balance<500:
            print("minimum balance should be ₹500")
        else:
            account={
                
            "account_no":account_no,
            "name":name,
            "balance":balance
            }
            self.accounts.append(account)
            print("account created successfully")
    def display_accounts(self):
        if self.accounts:
            for account in self.accounts:
                print(f"account no:{account['account_no']}")
                print(f"customer name:{account['name']}")
                print(f"balance :{account['balance']}")
                print("-------------------------")
        else:
            print("no accounts found")

    def search_account(self):
        account_no=int(input("enter the no to search:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                print(f"account no:{account['account_no']}")
                print(f"customer name:{account['name']}")
                print(f"balance :{account['balance']}")
                break
        else:
            print("account not exist")
    def update_account(self):
        account_no=int(input("enter the account no:"))
        for account in self.accounts:
            if  account['account_no']==account_no:
                print("1.update customer name")
                print("2.update account number")
                choice=int(input("enter the choice:"))
                if choice==1:
                    new_name=input("enter new name:")
                    account["name"]=new_name
                    print("customer name updated")
                elif choice==2:
                    new_acc_no=int(input("enter the new acc no:"))
                    for acc in self.accounts:
                        if acc['account_no']==new_acc_no:
                            print("account already exist")
                            break
                    else:
                        account['account_no']=new_acc_no
                        print("account number updated")
                break
        else:
            print("account not found")
    def deposite_amount(self):
        account_no=int(input("enter the account no:"))
        for account in self.accounts:
            if  account['account_no']==account_no:
                amount=float(input("enter deposite amount:"))
                if amount>0:
                    account['balance']+=amount
                    print(f"deposite amount:{amount}")
                    print(f"current amount:{account['balance']}")
                else:
                    print("deposite amount must be greater than 0")
                break
        else:
            print("account not found")

    def withdraw_amount(self):
        account_no=int(input("enter the acoount no:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                amount=float(input("enter the withdrawal amount:"))
                if amount>0:
                    if account['balance']-amount>500:
                        account['balance']-=amount
                        print(f"withdrawal amount:{amount}")
                        print(f"current balance:{account['balance']}")
                    else:
                        print("account must maintain minimum balance of ₹500")
                else:
                    print("withdrawal amount must greater than zero")
                return
        else:
            print("account not found ")

    def delete_account(self):
        account_no=int(input("enter the acc no:"))
        for account in self.accounts:
            if account['account_no']==account_no:
                if account['balance']>0:
                    print("account cannot be deleted")
                else:
                    self.accounts.remove(account)
                    print(f"account with account_no{account_no}")
                return
        else:
            print("account not found")

b1=Bank()

print("==========Bank Managment System==========")
while True:
    print("1.create account")
    print("2.display account")
    print("3.search account")
    print("4.update account")
    print("5.deposite")
    print("6.withdraw")
    print("7.delete account")
    print("8.exit")

    choice=int(input("enter the choice:"))
    if choice==1:
        b1.create_account()
        print("---------------")
    elif choice==2:
        b1.display_accounts()
        print("---------------")
    elif choice==3:
        b1.search_account()
        print("---------------")
    elif choice==4:
        b1.update_account()
        print("---------------")
    elif choice==5:
        b1.deposite_amount()
        print("---------------")
    elif choice==6:
        b1.withdraw_amount()
        print("---------------")
    elif choice==7:
        b1.delete_account()
        print("---------------")

