# Set Operations and Methods in Python

# 1. union() method: Returns a new set with elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)  # {1, 2, 3, 4, 5}
print("Union:", union_set)

# 2. update() method: Adds elements from another set to the original set.
set1.update(set2)  # set1 becomes {1, 2, 3, 4, 5}
print("Update:", set1)

# 3. intersection() method: Returns a new set with elements common to both sets.
set3 = {2, 3, 6}
intersection_set = set1.intersection(set3)  # {2, 3}
print("Intersection:", intersection_set)

# 4. intersection_update() method: Updates the original set with the common elements.
set1.intersection_update(set3)  # set1 becomes {2, 3}
print("Intersection Update:", set1)

# 5. symmetric_difference() method: Returns a new set with elements not common to both sets.
sym_diff_set = set2.symmetric_difference(set3)  # {1, 4, 5, 6}
print("Symmetric Difference:", sym_diff_set)

# 6. difference() method: Returns a new set with elements in the first set but not in the second.
diff_set = set2.difference(set3)  # {1, 4, 5}
print("Difference:", diff_set)

# 7. difference_update() method: Updates the original set by removing elements found in another set.
set2.difference_update(set3)  # set2 becomes {1, 4, 5}
print("Difference Update:", set2)

# 8. isdisjoint() method: Returns True if two sets have no elements in common.
disjoint_check = set1.isdisjoint(set2)  # True
print("Is Disjoint:", disjoint_check)

# 9. issuperset() method: Returns True if the set contains all elements of another set.
superset_check = set1.issuperset(set3)  # False
print("Is Superset:", superset_check)

# 10. issubset() method: Returns True if the set is contained within another set.
subset_check = set3.issubset(set1)  # True
print("Is Subset:", subset_check)

# 11. add() method: Adds a single element to the set.
set3.add(7)  # set3 becomes {2, 3, 6, 7}
print("Add:", set3)

# 12. remove() method: Removes a specific element from the set; raises KeyError if not found.
set3.remove(7)  # set3 becomes {2, 3, 6}
print("Remove:", set3)

# 13. discard() method: Removes a specific element from the set; does nothing if not found.
set3.discard(6)  # set3 becomes {2, 3}
print("Discard:", set3)

# Difference between remove() and discard():
# - remove() raises an error if the element does not exist.
# - discard() does nothing if the element does not exist.

# 14. del keyword: Deletes the entire set.
del set3  # set3 is deleted

# 15. clear() method: Removes all elements from the set.
set2.clear()  # set2 becomes an empty set {}
print("Clear:", set2)

# 16. 'in' keyword: Checks if an element is in the set.
check_in = 1 in set1  # True
print("'in' Check:", check_in)

# 17. 'not in' keyword: Checks if an element is not in the set.
check_not_in = 7 not in set1  # True
print("'not in' Check:", check_not_in)
