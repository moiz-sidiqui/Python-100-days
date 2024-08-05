# Recursion is a programming concept where a function calls itself to solve a problem.
# It breaks down a complex problem into smaller, more manageable sub-problems. 
# A recursive function typically has two main parts:

# Base Case: This is the condition that stops the recursion. It prevents the function
# from calling itself indefinitely.

# Recursive Case: This is the part of the function where it calls itself with a smaller or 
# simpler input.

# example

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage
print(factorial(5))  # Output: 120

