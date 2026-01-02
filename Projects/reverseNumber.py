# x = 12345
# y = ""
# num = str(x)
# for i in num:
#     y=i+y
# y1=int(y)
# print(y1)


# num = +1234
# rev = int(str(abs(num))[::-1])
# print(-rev)

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

print(reverse_num(12345))
