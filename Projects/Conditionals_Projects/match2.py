# Week days schedular

day= input("Enter your day : ").capitalize()

match day:
    case "Monday":
        print("Coding kare ho python")
    case "Tuesday":
        print("School HomeWork")
    case "Wenesday":
        print("Tuition")
    case "Thursday":
        print("circket")
    case "Frieday":
        print("Weekend Studies")
    case "Saturday":
        print("Romining")
    case "Sunday":
        print("Playing games")
    case _:
        print("Enter correct day")