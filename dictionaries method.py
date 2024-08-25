# Dictionary methods demonstration

# Creating a sample dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 1. update - Updates the dictionary with elements from another dictionary or iterable of key-value pairs.
my_dict.update({'d': 4})
print("After update:", my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 2. clear - Removes all items from the dictionary.
my_dict.clear()
print("After clear:", my_dict)  # Output: {}

# Re-creating the dictionary for further demonstration
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 3. pop - Removes and returns an item with the specified key. Raises KeyError if key is not found.
value = my_dict.pop('b')
print("Popped value:", value)  # Output: 2
print("After pop:", my_dict)   # Output: {'a': 1, 'c': 3}

# 4. popitem - Removes and returns the last inserted key-value pair as a tuple. Raises KeyError if the dictionary is empty.
item = my_dict.popitem()
print("Popped item:", item)    # Output: ('c', 3) or ('a', 1) depending on insertion order
print("After popitem:", my_dict)  # Output: {'a': 1} or {}

# 5. del - Deletes a key-value pair from the dictionary. Raises KeyError if the key is not found.
del my_dict['a']
print("After del:", my_dict)  # Output: {}

# Note: The dictionary is empty after 'del' operation so further operations may raise errors.
