'''
* W * * *
* W * * *
* W * * *
* W * * *
* W * * *

'''

for i in range(1,6): # row
    for j in range(1,6): # column
        if(j==2):
            print("W", end=" ")
        else:
            print("*", end=" ")
    print("\n")