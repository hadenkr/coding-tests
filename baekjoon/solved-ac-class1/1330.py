line = input()
array = line.split(maxsplit=2)
a, b = int(array[0]), int(array[1])
if a > b: print('>')
elif a < b: print('<')
else: print('==')
