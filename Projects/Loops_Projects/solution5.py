# 5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character

str1 = "HHellofgfg"


for x in str1:
    if str1.count(x)==1:
        print("Char is : ", x)
        break