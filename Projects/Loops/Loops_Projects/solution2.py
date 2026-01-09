# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = 10
sumofEven = 0
for num in range(1,n+1):
    if(num%2==0):
        sumofEven = sumofEven+num # 2+4+6+8+10 =30
print(sumofEven)


# problem : Calculate the sum of odd numbers up to a given number n.