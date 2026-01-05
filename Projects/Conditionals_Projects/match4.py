# ATM system

balance = 1000
pin = 1111
userPin = int(input("Enter UPI Pin : "))
if (userPin == pin):
            print("Pin is verified...\n")
            ch = int(input("___Welcome Apkaa ATM___ " \
            "\n1. balance" \
            "\n2. deposit" \
            "\n3. debit" \
            "\n4. exit " \
            "\n"))

            match ch:
                case 1:
                    print("Your Current_Balance is = rs.",balance)
                case 2:
                    deposit= int(input("Enter your Deposit Amount : "))
                    balance = deposit+balance
                    print("A/c Credited/depositd Amount of = rs.",deposit,"in Your Account.","Your Current_balance is : rs.",balance)
                case 3:
                    debit = int((input("Enter your Debit Amount : ")))
                    if(balance>0 and debit<balance):
                        balance = balance-debit
                        print("A/c balance debited amount of rs.",debit,"from Your current_balance is : rs.",balance )
                    else:
                        print("Insufficient Balance.")
                case 4:
                    print("Thanks for visit..")
                case _:
                    print("Enter correct request")
else:
        print("Incorrect Pin")
