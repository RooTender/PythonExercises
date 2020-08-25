import copy

# shallow copy
myArray = [1, 2, 3, [4, 5]]
shallowCopy = copy.copy(myArray)
print(myArray)
print(shallowCopy)

myArray[3][0] = 0 # shallow copy concerns only next dimensions
print(myArray)
print(shallowCopy)

deepCopy = copy.deepcopy(myArray)
myArray[3][0] = 4 # shallow copy concerns only next dimensions
print(myArray)
print(deepCopy)