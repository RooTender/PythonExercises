# (ad)just / center
print('Hello'.rjust(15))
print('World'.ljust(15) + '!')

print('Hello'.rjust(15, '.'))
print('World'.center(15, '='))


# strip
uglyString = '         Hi, there   '
print(uglyString.strip() + '.')
print(uglyString.lstrip() + '.')
print(uglyString.rstrip() + '.')