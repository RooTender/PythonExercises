myArray = [1, 2, 3, 4, 5]

# searching using index
print(myArray.index(3))

# adding to array
myArray.append(6)
print(myArray)

myArray.insert(2, 3)
print(myArray)

myArray.remove(3) # removes once!
print(myArray)

myArray.sort(reverse=True)
print(myArray)



lettersArray = ['a', 'z', 'A', 'Z']

# advanced
lettersArray.sort(key=str.lower)
print(lettersArray)
