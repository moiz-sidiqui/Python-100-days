# Dictionaries in Python

# A dictionary in Python is like a real-world dictionary.
# it stores key-value pairs. 
# Each key is unique
# You can use the key to retrieve its corresponding value.



# Example of a dictionary
my_dict = {
    'apple': 'a fruit',
    'car': 'a vehicle',
    'python': 'a programming language'

}


# Simple retrieval vs get method

# Simple retrieval:
# However, if the key does not exist, Python will raise a KeyError.

value = my_dict['apple']  # This will work fine
# value = my_dict['banana']  # This would raise a KeyError



# Get method:
# The get method is safer. It retrieves the value associated with the key, 
# but if the key does not exist, it returns None (or a default value if you specify one).

value_safe = my_dict.get('banana')  # This will return None, not an error
value_with_default = my_dict.get('banana', 'not found')  # This will return 'not found'

# .keys() method
# returns list of keys
keys = my_dict.keys()  # This will give you dict_keys(['apple', 'car', 'python'])


# .values() method
# list of all the values in the dictionary.

values = my_dict.values()  # This will give you dict_values(['a fruit', 'a vehicle', 'a programming language'])


# .items() method
# The .items() method returns a view object that displays a list of all the key-value pairs as tuples.

items = my_dict.items()  # This will give you dict_items([('apple', 'a fruit'), ('car', 'a vehicle'), ('python', 'a programming language')])

# Let's print the outputs for clarity

print("Value for 'apple' (simple retrieval):", value)
print("Value for 'banana' (using get method):", value_safe)
print("Value for 'banana' with default (using get method):", value_with_default)
print("Keys:", keys)
print("Values:", values)
print("Items:", items)


# output
# Value for 'apple' (simple retrieval): a fruit
# Value for 'banana' (using get method): None
# Value for 'banana' with default (using get method): not found
# Keys: dict_keys(['apple', 'car', 'python'])
# Values: dict_values(['a fruit', 'a vehicle', 'a programming language'])
# Items: dict_items([('apple', 'a fruit'), ('car', 'a vehicle'), ('python', 'a programming language')])

