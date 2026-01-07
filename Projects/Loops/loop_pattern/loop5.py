for i in range(1,6):
    for j in range(1,6):
        if i==1:
            print("@", end=" ")
        elif i==3:
            print("#", end=" ")
        elif i==5:
            print("0", end=" ")
        else :
            print("*", end=" ")
    print("\n")

'''
    Output:

@ @ @ @ @ 

* * * * * 

# # # # # 

* * * * * 

0 0 0 0 0 

'''