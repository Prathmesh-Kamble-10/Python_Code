for i in range(1,6):
    for j in range(1,6):
        if j==5:
            print("$ ", end=" ")
        elif j==2:
            print("W ", end=" ")
        elif i==1:
            print("@ ", end=" ")
        elif i==3:
            print("# ", end=" ")
        elif i==5:
            print("0 ", end=" ")
        else :
            print("* ", end=" ")
    print("\n")


'''
Output:

@  W  @  @  $  

*  W  *  *  $  

#  W  #  #  $  

*  W  *  *  $  

0  W  0  0  $  

'''