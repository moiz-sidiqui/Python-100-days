#string is like an array

# string[starting index : ending index]
# starting index is included
# ending index is not included


# print first name
name = 'Moiz Siddiqui'
print(name[0:4])

#output - Moiz

#use len function for knowing the length of the string
print(len(name))

#output - 13

#negative slicing starts from right with -1
print(name[0:-3])
#output - Moiz Siddi

# Note:
# [: -3] and [: len(string) -3] are equal

n='harry'
print(n[-4:-2])
#output - ar