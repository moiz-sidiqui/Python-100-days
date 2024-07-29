# List Methods Examples in Python

# Initial list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# append() - Adds an element at the end of the list
my_list.append(3)
print("After append(3):", my_list)
# Output: After append(3): [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# reverse() - Reverses the elements of the list in place
my_list.reverse()
print("After reverse():", my_list)
# Output: After reverse(): [3, 5, 6, 2, 9, 5, 1, 4, 1, 3]

# sort() - Sorts the list in ascending order
my_list.sort()
print("After sort():", my_list)
# Output: After sort(): [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# index() - Returns the index of the first element with the specified value
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)
# Output: Index of 4: 5

# count() - Returns the number of elements with the specified value
count_of_1 = my_list.count(1)
print("Count of 1:", count_of_1)
# Output: Count of 1: 2

# copy() - Returns a shallow copy of the list
my_list_copy = my_list.copy()
print("Shallow copy of the list:", my_list_copy)
# Output: Shallow copy of the list: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# insert() - Adds an element at the specified position
my_list.insert(2, 7)
print("After insert(2, 7):", my_list)
# Output: After insert(2, 7): [1, 1, 7, 2, 3, 3, 4, 5, 5, 6, 9]

# extend() - Adds the elements of a list (or any iterable) to the end of the current list
my_list.extend([8, 9, 10])
print("After extend([8, 9, 10]):", my_list)
# Output: After extend([8, 9, 10]): [1, 1, 7, 2, 3, 3, 4, 5, 5, 6, 9, 8, 9, 10]

# remove() - Removes the first item with the specified value
my_list.remove(5)
print("After remove(5):", my_list)
# Output: After remove(5): [1, 1, 7, 2, 3, 3, 4, 5, 6, 9, 8, 9, 10]

# pop() - Removes the element at the specified position
popped_element = my_list.pop(3)
print("After pop(3):", my_list)
print("Popped element:", popped_element)
# Output: After pop(3): [1, 1, 7, 3, 3, 4, 5, 6, 9, 8, 9, 10]
# Output: Popped element: 2

# clear() - Removes all elements from the list
my_list.clear()
print("After clear():", my_list)
# Output: After clear(): []

# demonstrating the copy() method again after clearing the list
print("Shallow copy (unchanged):", my_list_copy)
# Output: Shallow copy (unchanged): [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

# reinitialize the list for demonstration of remaining methods
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# len() - Returns the number of elements in the list (not a method, but useful for lists)
length_of_list = len(my_list)
print("Length of the list:", length_of_list)
# Output: Length of the list: 9

# max() - Returns the largest item in the list (not a method, but useful for lists)
max_item = max(my_list)
print("Max item in the list:", max_item)
# Output: Max item in the list: 9

# min() - Returns the smallest item in the list (not a method, but useful for lists)
min_item = min(my_list)
print("Min item in the list:", min_item)
# Output: Min item in the list: 1

# sum() - Returns the sum of all elements in the list (not a method, but useful for lists)
sum_of_list = sum(my_list)
print("Sum of the list:", sum_of_list)
# Output: Sum of the list: 36
