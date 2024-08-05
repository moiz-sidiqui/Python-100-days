# Question
# Write a recursive function to reverse a string. The function should take a string as input and return the 
# string in reverse order.

# Example:

# Input: "hello"

# Output: "olleh"


def reverse_string(str):

    if str=="" or len(str)==1:
        return str
    
    else:
        return reverse_string(str[1:]) + str[0]
    

print(reverse_string('hello'))
    