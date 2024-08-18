
# In Python, if is used to execute a block of code if a condition
#  is true. The elif (else if) and else statements provide additional 
#  conditions and a fallback block if no conditions are true, respectively.


# Example

# if condition1:
#     # code block
# elif condition2:
#     # another code block
# else:
#     # fallback code block


# conditional operators are used in conditions which are:
# < , > , <= , >= , == , !=


# nested if-elif-else

age = 25
country = "USA"

if country == "USA":
    if age >= 21:
        print("You can legally drink alcohol in the USA.")
    else:
        print("You cannot legally drink alcohol in the USA.")
else:
    if age >= 18:
        print("You can legally drink alcohol.")
    else:
        print("You cannot legally drink alcohol.")



