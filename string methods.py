# string are immutable - we cannot change them inplace.

str = 'Moiz'

print(str.upper())
#output - Moiz
print(str.lower())
#output - moiz

# Note: 
# existing strings are not changed new strings are made

# rstrip()
name = 'MoizZZZZZZZZ'
print(name.rstrip('Z'))

#output
#Z is stripped and removed.
#only triailing characters can be removed


# replace
# replaces All occurences of a string with a string
t = 'Moiz-----Moiz'
print(t.replace('Moiz','Ali'))

# output - Ali-----Ali

#split()
#splits the given string at the specified instance and returns separated string as list items
strr = 'Moiz Fatima Zainab'
b = strr.split(" ")
print(b)

# output - ['Moiz', 'Fatima', 'Zainab']


#capitalize()
# capitalizes only the first letter of the string and rest to lower case.
tt = 'introduction to Strings'
print(tt.capitalize())

#output - Introduction to strings


#center()
str3 = 'Welcome'
print(str3.center(20))

#it will give 20 spaces first
#output -'      Welcome'


#count()
str4 = 'Boommmm!!'
print(str4.count('m'))

#output - 4


#endswith()
# this method checks if the string ends with a given value.
# if yes returns True, else false

str5 = 'Welcome!!!!'
print(str5.endswith('!!!!'))

# output - True

#another example
str = 'Welcome to the Console'
print(str.endswith('to',4,10))  # 4, 10 are the slicing indices

#output - True


#find()
# searches first occurrences of a given value and returns its incex
# if given value is absent then returns -1

str = 'My name is moiz'
print(str.find('is'))

#output - 8
print(str.find('f'))

#output - -1

# we will use index() for same purpose but index()
# will throw an exception error: ValueError


#isalnum()
# returns True if only entire string consists of A-Z,a-z,0-9 (not space)
# returns False if any other character
str='Welcome to the console'
print(str.isalnum())

#output False
str='Welcometotheconsole'
print(str.isalnum())

#output True

#isalpha()
#returns True if A-z,a-z else False
str='Welcome'
print(str.isalpha())      # output True


#islower()
# True if all characters are in lower case else False
str='welcome'
print(str.islower())                  # output  True


#isprintable()
# returns true if all values are printable
# else False ( for \n)

str = 'moiz\n'
print(str.isprintable())    # False


#isspace()
# returns true if and only if string contains white spaces, else returns false
str ='         '
print(str.isspace())      # True
str = '   h   '
print(str.isspace())      # False



#istitle()
# returns true only if the first letter of each word of the string is capitalized,
# else false

str = 'Welcome Home'
print(str.istitle())    # True


#startswith()
str = 'welcome home'
print(str.startswith('welcome'))    # True



#swapcase()
# converts lower to upper and upper to lower case
str = 'Weather is Good'
print(str.swapcase())      # wEATHER IS gOOD

#title()
# all first letters are capitalized
str = 'my name is moiz'
print(str.title())      # My Name Is Moiz
