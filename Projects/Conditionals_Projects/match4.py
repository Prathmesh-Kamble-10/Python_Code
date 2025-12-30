# ATM system

balance = 1000

ch = input(" ATM " \
"\n1. balance" \
"\n2. deposit" \
"\n3. debit" \
" :\n ")
match ch:
    case "balance":
        print("Your Current_Balance is = rs.",balance)
    case "deposit":
        deposit= int(input("Enter your Deposit Amount : "))
        balance = deposit+balance
        print("A/c Credited/depositd Amount of = rs.",deposit,"in Your Account.","Your Current_balance is : rs.",balance)
    case "debit":
        debit = int((input("Enter your Debit Amount : ")))
        if(balance>0 and debit<balance):
            balance = balance-debit
            print("A/c balance debited amount of rs.",debit,"from Your current_balance is : rs.",balance )
        else:
            print("Insufficient Balance.")
    case _:
        print("Enter correct request")
