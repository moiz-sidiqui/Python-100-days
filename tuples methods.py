# Tuples in Python


# if we want to manipulate a tuple like append we need to convert it in list first and do the changes and then
# convert it back to tuple.

# 1. Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)  # Output: (1, 2, 3, 4, 5)



# 2. count() method
count_of_3 = my_tuple.count(3)
print("Count of 3 in my_tuple:", count_of_3)  # Output: 1



# 3. index() method
index_of_4 = my_tuple.index(4)
print("Index of 4 in my_tuple:", index_of_4)  # Output: 3



# 4. Slicing a tuple
slice_tuple = my_tuple[1:4]
print("Slice of my_tuple from index 1 to 3:", slice_tuple)  # Output: (2, 3, 4)



# 5. Concatenation of tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated Tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)



# 6. Attempting to append to a tuple (will raise an AttributeError)
try:
    my_tuple.append(6)
except AttributeError as e:
    print("Error:", e)  # Output: 'tuple' object has no attribute 'append'



# 7. Creating a new tuple by "appending"
new_tuple = my_tuple + (6,)
print("New Tuple after 'appending':", new_tuple)  # Output: (1, 2, 3, 4, 5, 6)



# 8. Operations on tuples
length_of_tuple = len(my_tuple)
print("Length of my_tuple:", length_of_tuple)  # Output: 5



max_value = max(my_tuple)
print("Max value in my_tuple:", max_value)  # Output: 5



min_value = min(my_tuple)
print("Min value in my_tuple:", min_value)  # Output: 1



# 9. Nesting tuples
nested_tuple = (my_tuple, another_tuple)
print("Nested Tuple:", nested_tuple)  # Output: ((1, 2, 3, 4, 5), (6, 7, 8))



# 10. Iterating through a tuple
print("Elements in my_tuple:")
for item in my_tuple:
    print(item)
# Output:
# 1
# 2
# 3
# 4
# 5



# 11. Unpacking tuples
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)  # Output: 1 2 3 4 5



# 12. Using tuples as keys in dictionaries
dict_with_tuple_key = {my_tuple: "tuple as key"}
print("Dictionary with tuple key:", dict_with_tuple_key)  # Output: {(1, 2, 3, 4, 5): 'tuple as key'}
