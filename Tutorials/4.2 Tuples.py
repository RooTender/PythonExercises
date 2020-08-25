myTuple = ('Hello', 'World', '!', 1, 2, 3, )
myArray = ['Hello', 'World', '!', 1, 2, 3]

print(myTuple)
print(myArray)

# Note the difference:
# lists CAN be modified
# tuples CANNOT be modified

# conversions
print(list(myTuple))
print(tuple(myArray))

print(list('Hello World!'))