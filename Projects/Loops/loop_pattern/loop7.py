'''
* W * * *
* W * * *
* W * * *
* W * * *
* W * * *

'''

for i in range(1,6):
    for j in range(1,6):
        if(j==2):
            print("W", end=" ")
        else:
            print("*", end=" ")
    print("\n")