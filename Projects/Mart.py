print("Welcome to the Market Place Application")
while True:

    print("""
        1.Electronics
        2.Clothing
        3.Groceries
        4.Exit
        """)

    ch=int(input("Enter Your Choice : "))

    if ch==1:
        print("""
            1.Mobile (Rs.15000/-)
            2.Laptop (Rs.35000/-)
            3.TV (Rs.10000/-)
            4.Exit
        """)
        ch1=int(input("Enter Your Choice : "))
        if ch1 == 1:
            price=15000
            print("You have selected Mobile")
        elif ch1==2:
            price=35000
            print("You have selected Laptop")
        elif ch1==3:
            price=10000
            print("You have selected Laptop")
        elif ch==4:
            print("Thanks for Visiting...")

    elif ch==2:
        print("""
            1.Shirt (Rs.1000/-)
            2.T-Shirt (Rs.450/-)
            3.Pant (Rs.1500/-)
            4.Exit
        """)
        ch1=int(input("Enter Your Choice : "))
        if ch1 == 1:
            price=1000
            print("You have selected Shirt")
        elif ch1==2:
            price=450
            print("You have selected T-Shirt")
        elif ch1==3:
            price=1500
            print("You have selected Pant")
        elif ch==4:
            print("Thanks for Visiting...")

    elif ch==3:
        print("""
            1.Wheat 1kg (Rs.38/-)
            2.Sugar 1kg (Rs.40/-)
            3.ChaiPati 500g (Rs.30/-)
            4.Exit
        """)
        ch1=int(input("Enter Your Choice : "))
        if ch1 == 1:
            price=38
            print("You have selected Wheat")
        elif ch1==2:
            price=40
            print("You have selected Sugar")
        elif ch1==3:
            price=30
            print("You have selected ChaiPati")
        elif ch==4:
            print("Thanks for Visiting...")

    elif ch ==4:
            print("Thanks for Visiting...")
            break

    else:
        print("invalid Choice")

    qty = int(input("Enter the quantity : "))

    total = price*qty

    if total>30000:
        discount=total*0.12
        print("You have got 12% discount")
    elif total>15000:
        discount = total*0.8
        print("You have got 8% discount")
    else:
        discount = 0
        print("No discount")
        
    finalAmount = total-discount
    print("Your got discount",discount)
    print("Your Bill is, Rs.",finalAmount)
    print("Keep shopping with Market Place")