# simple calculator

a = int(input("Enter your First Number : "))
b = int(input("Enter your First Number : "))
result=0

ch = input("Enter your Choice('+','-','*','/','%') : ")
match ch:
    case "+":
            result = a+b
            print("Your Addition is = ",result)
    case "-":
            result = a-b
            print("Your Subtraction is = ",result)
    case "*":
            result = a*b
            print("Your Multiplication is = ",result)
    case "/":
            result = a/b
            print("Your Division is = ",result)
    case "%":
            result = a%b
            print("Your Mod is = ",result)
    case _:
            print("Enter correct choice")