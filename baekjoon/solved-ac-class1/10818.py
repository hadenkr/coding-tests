import sys

number = int(sys.stdin.readline().rstrip())
values = map(int, sys.stdin.readline().rstrip().split(maxsplit=number-1))

for index, value in enumerate(values):
    if index == 0:
        result = (value, value)
    elif value > result[1]:
        result = (result[0], value)
    elif value < result[0]:
        result = (value, result[1])

print('{} {}'.format(result[0], result[1]))
