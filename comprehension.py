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

names = ["A", "B", "C"]
marks = [70, 80, 90]

result = {name: mark for name, mark in zip(names, marks)}
print(result)