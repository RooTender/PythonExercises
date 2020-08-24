# printing text
x = 3
y = 4
print(str(x) + ', ' + str(y))
print("{0}, {1}".format(x, y))

# multipling text
spam = 'spam'
print(spam * 3)

# getting input
print('Hi! What\'s your name?')
myName = input()

print('Nice name, ' + myName + '.')
print('It has ' + str(len(myName)) + ' letters!')

# given input is ALWAYS a string
print('Give me a number')
myNumber = input()

myNumber = int(myNumber)
print(myNumber)