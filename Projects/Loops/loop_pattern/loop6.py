"""

*  *  *  *  *  

*  #  #  #  *  

*  #  #  #  *

*  #  #  #  *

*  *  *  *  *

"""

for i in range(1,6):
    for j in range(1,6):
        if((j==2 and i==2) or (i==2 and j==3) or (i==2 and j==4)):
            print("#", end=" ")
        elif((j==2 and i==3) or (i==3 and j==3) or (i==3 and j==4)):
            print("#", end=" ")
        elif((j==2 and i==4) or (i==4 and j==3) or (i==4 and j==4)):
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()