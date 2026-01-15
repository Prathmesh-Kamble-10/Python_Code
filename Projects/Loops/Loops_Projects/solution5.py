# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character

str1 = "HHellofgfg"

for x in str1:
    if str1.count(x)==1: # str1.count("H")==1
        print("Char is : ", x)
        break

# Problem: Given a string, find the non-repeated character
str2="Hello, Welcome to www.myWord.com"

