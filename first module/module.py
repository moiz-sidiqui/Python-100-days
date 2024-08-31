print('First Module')

#python creates a __main__ variable

if __name__ == '__main__':
    print('You are in the module.')
else:
    print('You are in the main and the name of the file is: ',__name__)



# output
# First Module 
# You are in the module.



# Note:
# if we dont want someone to access our module file then:

# import sys
# if __name__ == '__main__':
#     print('dont access.')
#     sys.exit()