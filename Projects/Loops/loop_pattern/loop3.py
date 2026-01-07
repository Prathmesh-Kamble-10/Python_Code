rows = int(input("Enter the rows count: "))
col = int(input("Enter the col count: "))
for i in range(1,rows+1):
    for j in range(1,col+1):
        if(i==3):
            print("# ",end=" ")
        else:
            print("* ",end=" ")
    print("\n")

"""
Ouput:=

*  *  *  *  *  

*  *  *  *  *  

#  #  #  #  #

*  *  *  *  *

*  *  *  *  *
"""