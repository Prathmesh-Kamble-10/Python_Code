rows = int(input("Enter the row size for the pattern: ")) #5
col=int(input("Enter the column size for the pattern: ")) #5
for i in range(1, rows + 1):  # Outer loop for rows   
    for j in range(1, col + 1):  # Inner loop for columns
        print(i, end=" ")   # Print star
    print("\n")

# ouptput : 

    # 1 1 1  
    # 2 2 2 
    # 3 3 3 
