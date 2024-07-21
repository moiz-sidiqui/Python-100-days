# In Python, match statements (introduced in Python 3.10) allow 
# pattern matching, similar to switch-case statements in other 
# languages, to execute code blocks based on the value of a variable.

# Example

status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case _:                   #default - a type of else
        print("Unknown status")


# output - Not Found

# Note: if one case statement is executed then no other case 
# statements are executed




