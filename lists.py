# lists_explanation.py

# Lists in Python
# A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.

# Creating a list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
# Output: Original list: [1, 2, 3, 4, 5]

# Lists can contain items of different types
mixed_list = [1, "Hello", 3.4, True]
print("Mixed list:", mixed_list)
# Output: Mixed list: [1, 'Hello', 3.4, True]

# Accessing items in a list
print("First item:", my_list[0])  # Lists are zero-indexed
# Output: First item: 1

# Modifying items in a list
my_list[1] = 200
print("Modified list:", my_list)
# Output: Modified list: [1, 200, 3, 4, 5]

# Adding items to a list
my_list.append(6)
print("List after append:", my_list)
# Output: List after append: [1, 200, 3, 4, 5, 6]

# Removing items from a list
my_list.remove(200)
print("List after remove:", my_list)
# Output: List after remove: [1, 3, 4, 5, 6]

# Slicing in Python
# Slicing allows you to extract a portion of a list by specifying a start and end index.

# Slicing a list
slice_list = my_list[1:4]  # Extracts items from index 1 to 3 (end index is not included)
print("Sliced list (index 1 to 3):", slice_list)
# Output: Sliced list (index 1 to 3): [3, 4, 5]

# Omitting the start index implies starting from the beginning
print("Sliced list (start to index 2):", my_list[:3])
# Output: Sliced list (start to index 2): [1, 3, 4]

# Omitting the end index implies going till the end of the list
print("Sliced list (index 2 to end):", my_list[2:])
# Output: Sliced list (index 2 to end): [4, 5, 6]

# Using negative indices for slicing
print("Sliced list (last two elements):", my_list[-2:])
# Output: Sliced list (last two elements): [5, 6]

# List Comprehension
# List comprehensions provide a concise way to create lists.
# It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

# Creating a list of squares using list comprehension
squares = [x**2 for x in range(10)]
print("List of squares (0 to 9):", squares)
# Output: List of squares (0 to 9): [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Using if condition in list comprehension
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("List of even squares (0 to 9):", even_squares)
# Output: List of even squares (0 to 9): [0, 4, 16, 36, 64]

# Nested list comprehension for creating a matrix
matrix = [[j for j in range(5)] for i in range(5)]
print("5x5 matrix:")
for row in matrix:
    print(row)
# Output:
# 5x5 matrix:
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]

# Combining list comprehension with slicing
# Example: Create a list of squares of even numbers from an existing list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_squared = [x**2 for x in numbers if x % 2 == 0]
print("Squares of even numbers in the list:", even_numbers_squared)
# Output: Squares of even numbers in the list: [4, 16, 36, 64, 100]
