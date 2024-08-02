# Docstrings in Python are special strings used to document your code. 
# They provide a way to describe what a function, class, or module does, helping 
# others (and yourself) understand the code's purpose and usage. Docstrings are 
# written as the first statement inside a function, method, class, or module, and are 
# enclosed in triple quotes (""" """ or ''' '''). They can span multiple lines and 
# are accessible via the __doc__ attribute.


def add(a, b):
    
    """
    This function takes two numbers and returns their sum.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The sum of the two numbers.
    """
    return a + b

# Accessing the docstring
print(add.__doc__)
print(add(4,6))




# Note: the docstring must start right after the function defination otherwise the 
#       output of print(add.__doc__) would be None.