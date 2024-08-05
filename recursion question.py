# Question
# Write a recursive function to find the sum of all elements in 
# a list of integers. The function should take a list as input and return 
# the sum of its elements.


def sum_list(lst):
    if len(lst) ==0:
        return 1
    
    elif len(lst) == 1:
        return lst[0]
    
    else:
        return sum_list(lst[1:]) + lst[0]
    

l = [1, 2, 3, 4, 5]
print(sum_list(l))
        

    
    