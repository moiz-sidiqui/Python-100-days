# A while loop in Python repeatedly executes a block of code as long as
# a specified condition is true. It's commonly used to prompt for user 
# input until a certain condition is met.

#example

password = ""
while password != "secret":
    password = input("Enter the password: ")
print("Access granted.")

#In this example, the loop continues asking for the password until the correct one ("secret") is entered.


# example input
# Enter the password: f
# Enter the password: fdfdf
# Enter the password: dfdfd
# Enter the password: dsfddfsfsfdsf
# Enter the password: secret
# Access granted.

