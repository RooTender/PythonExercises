def collatz(number):
    print(number)
    if (number > 1):
        
        if number % 2 == 0:
            collatz(number // 2)
        else:
            collatz(3 * number + 1)

myNumber = input()
collatz(int(myNumber))