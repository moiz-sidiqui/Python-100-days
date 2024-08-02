# f-strings, also known as formatted string literals, are a way to embed expressions inside
# string literals using curly braces {}. They provide a concise and readable way to include 
# variables or expressions within a string. Introduced in Python 3.6, f-strings are prefixed with the 
# letter f or F before the opening quotation mark.

#example 1

name = "Alice"
age = 30

greeting = f"Hello, my name is {name} and I am {age} years old."

print(greeting)

# Hello, my name is Alice and I am 30 years old.

# example 2

a = 5
b = 3
result = f"The sum of {a} and {b} is {a + b}."

print(result)

# The sum of 5 and 3 is 8.
