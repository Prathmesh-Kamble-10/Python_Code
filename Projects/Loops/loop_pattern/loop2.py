rows = int(input("Enter the row size for the pattern: "))
col=int(input("Enter the column size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, col + 1):  # Inner loop for columns
        print("* ", end=" ")   # Print star
    print("\n")

# output : 
    # * * *
    # * * *
    # * * *
