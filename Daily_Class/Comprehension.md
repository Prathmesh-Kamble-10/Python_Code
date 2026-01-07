# Python Comprehensions – Complete Guide (Beginner Friendly)

Python **comprehensions** are a short, clean, and Pythonic way to create collections  
(lists, sets, dictionaries, generators) in **one line** instead of writing long loops.

---

## What is a Comprehension?

A comprehension:
- Creates a new collection
- Uses a single line
- Replaces `for` loops + optional `if` conditions
- Makes code cleaner and more readable

---

## 1. List Comprehension

### Syntax
```python
[expression for item in iterable if condition]
```
### Example (Without Comprehension)
```python
squares = []
for i in range(5):
    squares.append(i * i)
```
### With Comprehension
```python
squares = [i * i for i in range(5)]
print(squares)
```
### output
```
[0, 1, 4, 9, 16]
```

### With Condition
```python
even_squares = [i * i for i in range(10) if i % 2 == 0]
print(even_squares)
```

### Using if-else
```python
result = ["even" if i % 2 == 0 else "odd" for i in range(5)]
print(result)
```
#### Note: if-else comes before for

## 2. Set Comprehension

### Syntax

```python
{expression for item in iterable}
```

### example
```python
nums = [1, 2, 2, 3, 4, 4]
unique_squares = {x * x for x in nums}
print(unique_squares)
```

### output
```
{1, 4, 9, 16}
```
#### Sets automatically remove duplicates

## 3. Dictionary Comprehension

### Syntax

```python
{key: value for item in iterable if condition}
```

### Example
```python
names = ["A", "B", "C"]
marks = [70, 80, 90]

result = {name: mark for name, mark in zip(names, marks)}
print(result)
```

### with conditional
```python
passed = {name: m for name, m in result.items() if m >= 75}
print(passed)
```

## 4. Generator Comprehension

### Syntax

```python
(expression for item in iterable)
```
### Example

```python
gen = (i * i for i in range(5))
print(gen)
```
```python
for value in gen:
    print(value)
```
#### Generators are memory efficient (best for large data)

## 5. Nested Comprehension
### Example

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)
```

### Output

```
[1, 2, 3, 4, 5, 6]
```

## 6. Using enumerate() in Comprehension

```python
fruits = ["apple", "banana", "mango"]
result = [f"{i}: {fruit}" for i, fruit in enumerate(fruits)]
print(result)
```

## 7. Using zip() in Comprehension

```python
names = ["A", "B", "C"]
marks = [60, 70, 80]

passed = [name for name, m in zip(names, marks) if m >= 70]
print(passed)
```
## 8. Using Walrus Operator (:=) in Comprehension

```python
nums = [10, 20, 30]
result = [y for x in nums if (y := x * 2) > 30]
print(result)
```
#### := assigns and uses the value in the same expression
Requires Python 3.8+