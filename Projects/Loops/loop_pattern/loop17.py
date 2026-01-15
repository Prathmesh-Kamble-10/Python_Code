# userInput = int(input("Enter your nth number: "))
# for num in range(1,userInput+1):
#     if(num%2!=0):
#         print("odd no = ",num)
#     else:
#         print("even no = ",num)



# for i in range(1,11):
#     for j in range(1,i+1):
#         for x in range (1,j+1):
#             print("x", end=" ")
#         for w in range (j,1):
#             print("x", end=" ")
#         print("*")
#     print("\n")


# for i in range(1,11):
#     for j in range(1,i+1):
#         for x in range (1,j+1):
#             print("x", end=" ")
#         print("*")

def print_modified_pascal(rows):
    triangle = [[7]]

    for i in range(1, rows):
        row = [7]
        prev_row = triangle[i - 1]

        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])

        row.append(7)
        triangle.append(row)

    max_width = len(''.join(map(str, triangle[-1])))

    for row in triangle:
        row_str = ' '.join(map(str, row))
        print(row_str.center(max_width))


if __name__ == "__main__":
    print_modified_pascal(6)