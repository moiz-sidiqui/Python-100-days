# Typecasting - The conversion of one data type into another data type
# we can use - int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict()

#explicit typecasting
a= '1'
b= '2'
print(a+b)

#output = 12

#if we want 3 we would have to typecast
print(int(a) + int(b))

# output 3


#implicit typecasting
#python converts a smaller data type to a higher data type to prevent data loss

#python converts a to int- automatically
a=7
#python converts b to float- automatically
b=8.8


#python converts c to float- automatically
c=a+b
print(a+b)
#15.8





