# dictionary
person = {'name': 'John', 'surname': 'Smith', 'height': 185}
print(person['name'])

# keys, values, items
for key in person.keys():
    print(key)
print(list(person.keys()))

for value in person.values():
    print(value)
print(list(person.values()))


for k, v in person.items():
    print(k + ': ' + str(v))


# get, setdefault
print(person.get('name', 'undefined var \'name\''))
print(person.get('age', 'undefined var \'age\''))

person.setdefault('age', 20)
print(person)