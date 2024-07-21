# In Python, functions can take four types of arguments: 
# positional arguments, keyword arguments, default arguments, and 
# variable-length arguments.


# Positional Arguments: Arguments passed to a function based on their position.

def add(a, b):
    return a + b
print(add(2, 3))  # Output: 5



# Keyword Arguments: Arguments passed to a function by explicitly specifying the parameter name.
def greet(name, greeting):
    return f"{greeting}, {name}!"
print(greet(name="Moiz", greeting="Hello"))  # Output: Hello, Alice!



# Default Arguments: Arguments that assume a default value if no value is provided in the function call.

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Moiz"))  # Output: Hello, Alice!
