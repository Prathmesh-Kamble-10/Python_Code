# 🔹 What does := do?

# := assigns a value to a variable AND returns that value at the same time.

# Normally:
a = 5
b = 2

remainder = a % b
if remainder != 0:
    print(remainder)


# With :=:

if (remainder := a % b) != 0:
    print(remainder)

# The value of a % b is stored in remainder and used in the condition.


# example : 2)

# normal way :

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# using walrus (:=)

# value = 15

# if remainder := value % 5:
#     print(f"Not divisible, remainder is {remainder}")


