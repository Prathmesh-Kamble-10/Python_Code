# Password strength check
# problem : Check if a Password is "Weak", "Medium", or "Strong". Criteria < 6 chars (Weak), 6-10 chars (Medium), > 10 chars (Strong)

pwd = input("Enter your password : ")
len_pwd = len(pwd)


if len_pwd < 6:
    print("Password is Weak")
elif len_pwd < 10:
    print("Password is Medium")
else:
    print("Password is Strong")