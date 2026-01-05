# no = 12345 #"12345"
# y = ""
# numStr = str(no)
# for i in numStr:
#     y=i+y # "54321" 
# numInt=int(y)
# print(numInt) #54321


# num = -1234

# traditional way
# positiveNum = abs(num)
# numstr = str(positiveNum)
# revStr = numstr[::-1]
# revNum = int(revStr)
# print(-revNum)

# comphrension way
# rev = int(str(abs(num))[::-1]) # 4321
# print(-rev)

# def reverse_num(n, rev=0):
#     if n == 0:
#         return rev
#     return reverse_num(n // 10, rev * 10 + n % 10)

# print(reverse_num(12345))
