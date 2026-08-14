import sys

def main():

    accounts = {
        "1001": {
            "name": "alice",
            "balance": 1250.00,
            "transactions": []
        },
        "1002": {
            "name": "bob",
            "balance": 840.50,
            "transactions": []
        },
        "1003": {
            "name": "jon",
            "balance": 2200.00,
            "transactions": []
        }
    }
    
    while True:
        
        menu = """
            Choose a menu option:

            (1) View Account Balance
            (2) Deposit Funds
            (3) Withdraw Funds
            (4) Transfer Funds
            (5) View Transaction History
            (6) View Bank Statistics
            (7) Exit
            """
        print(menu)
        
        escape = True
        while escape:

            users_name = input("What is your username? ")
            users_choice = input("What are you trying to do? Enter a number. ")

            validate_membership = []
            acc_id = ""
            for account in accounts.keys():
                if users_name in accounts[account]["name"]:
                    validate_membership.append(users_name)
                    acc_id = account

            if not validate_membership:
                continue

            try:
                users_choice = int(users_choice)
            except:
                print('Your choice must be a number.')
                continue
            
            escape = False

        if users_choice == 1:
            account_info(accounts, acc_id)
        elif users_choice == 2:
            deposit(accounts, acc_id)
        elif users_choice == 3:
            withdrawal(accounts, acc_id)
        elif users_choice == 4:
            transfer(accounts, acc_id)
        elif users_choice == 5:
            show_transaction_logs(accounts, acc_id)
        elif users_choice == 6:
            show_bank_info()
        elif users_choice == 7:
            print("See you next time!")
            sys.exit()
        else:
            continue

def account_info(accounts, acc_id):
    user_account = accounts[acc_id]["name"]
    balance = accounts[acc_id]["balance"]
    print(f"{user_account}'s balance is: {balance}")

def deposit(accounts, acc_id):
    while True:
        deposit_amount = input(
            "Enter the amount you'd like to deposit: $"
            )
        try:
            deposit_amount = abs(float(deposit_amount))
        except:
            print("Enter a valid decimal number")
            continue
        if deposit_amount == 0:
            print("Input must be larger than 0")
            continue
        break
    accounts[acc_id]['balance'] += abs(deposit_amount)
    print(f'Your new balance is: {accounts[acc_id]['balance']}')
    accounts[acc_id]['transactions'].append(f"Deposited {deposit_amount}")

def withdrawal(accounts, acc_id):
    while True:
        withdrawal_amount = input(
            "Enter the amount you'd like to withdraw: $"
        )
        try:
            withdrawal_amount = abs(float(withdrawal_amount))
        except:
            print("Enter a valid decimal number")
            continue
        if withdrawal_amount == 0:
            print("Input must be larger than 0")
            continue
        break
    accounts[acc_id]['balance'] -= withdrawal_amount
    if accounts[acc_id]['balance'] >= 0:
        print(f'Your new balance is: {accounts[acc_id]['balance']}')
        accounts[acc_id]['transactions'].append(f"Withdrew {withdrawal_amount}")
    else:
        accounts[acc_id]['balance'] += withdrawal_amount
        print("Insufficient Balance")

def transfer(accounts, acc_id):
    while True:
        transfer_amount = input(
            "Enter the amount you'd like to transfer: $"
        )
        try:
            transfer_amount = abs(float(transfer_amount))
        except:
            print("Enter a valid decimal number")
            continue
        if transfer_amount == 0:
            print("Input must be larger than 0")
            continue
        break

    while True:
        transfer_dest = input(
            "Who are you transferring money to? "
        )
        dest = ''
        for customer_id in accounts.keys():
            if transfer_dest in accounts[customer_id]['name']:
                dest = customer_id
        if dest:
            break
        else:
            print("User not available for transfer.")
            continue

    if dest != acc_id:
        accounts[acc_id]['balance'] -= transfer_amount
        if accounts[acc_id]['balance'] >= 0:
            print(f'Transfer to {transfer_dest} successful!')
            print(f'Your new balance is: {accounts[acc_id]['balance']}')
            accounts[dest]['balance'] += transfer_amount
            accounts[acc_id]['transactions'].append(f"{transfer_amount} send to {transfer_dest}")
            accounts[dest]['transactions'].append(f"{transfer_amount} received")
        else:
            accounts[acc_id]['balance'] += transfer_amount
            print("Insufficient Balance")
    else:
        print("You cannot transfer money to yourself")
    
def show_transaction_logs(accounts, acc_id):
    trans = accounts[acc_id]['transactions']
    print(trans)

def show_bank_info():
    print(
        """
    Bank Name is: Some Bank
    Bank founded in 2026
    I don't know what else to put here.
    """
    )

if __name__ == '__main__':
    main()