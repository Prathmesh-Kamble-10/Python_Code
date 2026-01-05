# 1 while loop

# x = 1
# twoTable = []
# while x<=10:
#     twoTable.append(x*2)
#     x = x+1
# print(twoTable)

# # infinite loop
# count = 1
# while True:
#     if(count<=10):
#         print("Hello",count)
#         count=count+1
#     else:
#         break


# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i = i+1

# username  pwd



while True:
    username = input("Enter your User Name : ")
    password = input("Enter your User password : ")
    if(username == "shubham" and password == "123456"):
            print("User login")
            break
    else:            
        print("Invalid Username and Password")