def simpleMath(num):
    """Outer function that creates and returns a number as square closure."""
    def power(power):
        """Inner function (closure) that remembers 'power'."""
        result = num ** power
        return result
    return (power) 

# Create two closures, each with a different 'factor' remembered
val1 = simpleMath(3)
val2 = simpleMath(5)
val3 = simpleMath(2)

# Use the closures
print(f"3 * 2 = {val1(2)}")
print(f"5 * 3 = {val2(3)}")
print(f"2 * 10 = {val3(10)}")

