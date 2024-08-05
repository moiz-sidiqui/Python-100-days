# Set in Python

# Unique Elements: No duplicates.
# Unordered Collection: No specific order.
# Mutable: Can be changed.
# Iterable: Can be looped.
# No Indexing: Access via iteration.

# Creating a set
my_set = {1, 2, 3, 4, 5,4,4,4,4,4}  # no duplicates
print(my_set)

# {1, 2, 3, 4, 5}


# accessing elements  order doesnot matters
for element in my_set:
    print(element)



#if we want to use indexing we have to convert it into lists
my_list = list(my_set)
print(my_list[0])  # Access first element
# 1