# do NOT modificate
print(r'Hello \'World\'!')

# many lines
print('''
Hello
there~!

How are you
DOING?
''')

# in / not in
str1 = "Hi"
str2 = "Hi, there!"

print(str1 in str2)
print(str2 in str1)

# upper / lower
print(str2.upper())
print(str2.isupper())


# startswith / endswith
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('!'))


# split / join
myString = 'This is my saxy string. I like this string very much.'
print(myString)

myList = myString.split()
print(myList)

print(' - '.join(myList))