def factorial(no): #3
    if(no==0):
        return 1
    else:
        return no*factorial(no-1) #5*4*3*2*1 

print(factorial(5))
''