def sayHello():
    print('Hello!')

for i in range(5):
    sayHello()


# overloading functions & arguments
def sayHello(name):
    print('Hello, {0}!'.format(name))

print('Your name?')
myName = input()

sayHello(myName)


# returns
def getFactorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(getFactorial(5))


# using global
def sayMyVariable():
    global myVar
    myVar = 'boom!'
    print(myVar)

sayMyVariable()
print(myVar)


# try & EXCEPT
def divideBy(number, by):
    try:
        return number / by
    except ZeroDivisionError:
        print('Division by ZERO!')
        return 0

print(divideBy(9, 3))
print(divideBy(9, 0))