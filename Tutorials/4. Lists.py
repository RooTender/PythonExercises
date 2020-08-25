# lists
listExample = [1, 2, 3]
print(listExample)
print(type(listExample))

animals = ['cat', 'dog', 'snake', 'tiger']
print(animals[-1])
print(animals[0:2])
print(animals[0:-1])
print(animals[2:])

del animals[2]
print(animals)

animals *= 2
print(animals)


list2D = [['a', 'b'], ['c', 'd']]
print(list2D[1][1])
print(len(list2D)) # list2D[0]


# small exercise
names = []
for i in range(5):
    print('Enter name: ', end='')
    name = input()
    names += [name] # notice square brackets!

print(names)

# in / not in
if 'name' in names:
    print('There\'s \'name\' in array \'names\'')
else:
    print('nevermind...')