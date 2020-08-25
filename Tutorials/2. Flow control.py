# boolean values are **Capitalized**
print(True and False or 0)


# if / elif / else
print('How old are you?')
myAge = input()
myAge = int(myAge)

if myAge < 18:
    print('You\'re pretty young')
elif myAge < 60:
    print('Oh, an adult!')
else:
    print('Oldie but goodie ;)')


# loops

## while ##
i = 0
while i < 10:
    i = i + 1
    print(i)

    if i == 5:
        break
print()

## for ##
for j in range(5):
    print(j)
print()

for j in range(2, 5):
    print(j)
print()

### range( start , end , iteration )
for j in range(5, -1, -1):
    print(j)
print()

# extra: import
import random, sys
print(random.randint(1, 10))

# extra: sys.exit()
sys.exit()