# In Python, a while loop can have an else block that executes when the loop 
# condition becomes false (and not when the loop is terminated by a break statement).

count = 0
while count < 5:
    count += 1
    print("Counting:", count)
else:
    print("Finished counting up to 5.")



# output
# Counting: 1
# Counting: 2
# Counting: 3
# Counting: 4
# Counting: 5
# Finished counting up to 5.