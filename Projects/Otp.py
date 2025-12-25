import random
OTP = ""
def OtpGenerator():
    global OTP
    for x in range(6):
        OTP+=str(random.randint(0,9))
    return OTP

def OtpValidator(userInput):
    if OTP == userInput:
        print("login")
    else :
        print("Invalid OTP")

def main():
    print("Your One Time Pwd :",OtpGenerator())
    userInput = input("Enter OTP : ")
    OtpValidator(userInput)

main()