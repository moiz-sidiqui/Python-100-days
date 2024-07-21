
# In Python, the break statement exits a loop prematurely when a specific
# condition is met, while the continue statement skips the rest of the current 
# loop iteration and moves to the next one.


# Example using 'break':

for number in range(10):
    if number == 5:
        break
    print(number)

# output
# 0
# 1
# 2
# 3
# 4


# Example using 'continue':

for number in range(10):
    if number % 2 == 0:
        continue
    print(number)


# output
# 1
# 3
# 5
# 7
# 9

# In the break example, the loop stops when number is 5. 
# In the continue example, the loop skips even numbers and only prints odd numbers.