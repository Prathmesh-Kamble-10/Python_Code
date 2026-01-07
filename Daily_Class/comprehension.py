# squares = []
# for i in range(5): # 1,2,3,4,5
#     squares.append(i * i)
# print(squares)


# [expression for item in iterable if condition]

# squares = [i * 2 for i in range(1,11)] 
# print(squares)



# for i in range(1,11):
#     if(i%2==0):
#         i=i*i
#         print(i)

# even_squares = [i * i for i in range(1,11) if i % 2 == 0] 
# print(even_squares)

# for num in range(1,11):
#     if(num%2==0):
#         print(tuple(f" Even : {num}"))
#     else:
#         print(tuple(f" Odd : {num}"))


# result = [f"even : {i}" if i % 2 == 0 else f"odd : {i}" for i in range(1,11)]
# print(result)

# nums = [1, 2, 2, 3, 4, 4]
# unique_squares = {x * x for x in nums}
# print(unique_squares)

# names = ["A", "B", "C","D"]
# marks = [70, 80, 90, 95]

# result = {name: mark for name, mark in zip(names, marks)} #{'A': 70, 'B': 80, 'C': 90, 'D':95}
# passed = {name: m for name, m in result.items() if m >= 90}
# print(passed)

# # print(result)

# gen = [i * i for i in range(0,6)]
# # print(gen)

# for value in gen:
#     print(value)

# matrix = [[1, 2], [3, 4], [5, 6]]


# flat = [num for row in matrix for num in row]
# print(flat)

# list1=[]
# for row in matrix:
#     for num in row:
#         list1.append(num)
# print(list1)


# # enumerate()
# fruits = ["apple", "banana", "mango"]
# # result = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]

# for i,fname in enumerate(fruits,start=1):
#     print(i,fname)
# # print(result)

# names = ["A", "B", "C"]
# marks = [60, 70, 80]

# passed = [name for name, m in zip(names, marks) if m >= 70]
# print(passed)

# list1 = []
# for n, m in zip(names,marks):
#     if(m>=70):
#         list1.append(n)
# print(list1)

# nums = [10, 20, 30]
# result = [y for x in nums if (y := x * 2) > 30]
# print(result)
