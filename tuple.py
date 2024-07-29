# Tuples in Python

# Tuples are like lists but cannot be changed after creation.
# They are used to store multiple items in a single variable.

# Creating a tuple
my_tuple = (1, "apple", 3.14)

# Accessing elements in a tuple
print("First item:", my_tuple[0])  # Output: 1
print("Second item:", my_tuple[1])  # Output: apple

# Tuples can contain different data types
mixed_tuple = (42, "hello", True, 3.14)
print("Mixed tuple:", mixed_tuple)  # Output: (42, 'hello', True, 3.14)

# Tuples can be nested
nested_tuple = (1, (2, 3), ("a", "b"))
print("Nested tuple:", nested_tuple)  # Output: (1, (2, 3), ('a', 'b'))

# Tuples support slicing
print("Slice of tuple:", my_tuple[1:3])  # Output: ('apple', 3.14)

# Trying to change an element in a tuple will raise an error
# my_tuple[1] = "orange"  # Uncommenting this line will raise a TypeError

# Tuples can be created without parentheses
another_tuple = 2, "banana", 4.56
print("Another tuple:", another_tuple)  # Output: (2, 'banana', 4.56)

# Tuples with one item need a comma
single_item_tuple = (5,)
print("Single item tuple:", single_item_tuple)  # Output: (5,)

# Length of a tuple
print("Length of my_tuple:", len(my_tuple))  # Output: 3

# Using tuples in a for loop
for item in my_tuple:
    print("Item:", item)
# Output:
# Item: 1
# Item: apple
# Item: 3.14

# Tuples can be used as keys in dictionaries because they are immutable
my_dict = {("key1", "key2"): "value"}
print("Dictionary with tuple key:", my_dict)  # Output: {('key1', 'key2'): 'value'}
