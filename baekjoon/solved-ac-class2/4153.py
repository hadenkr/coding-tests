import sys

def square(number):
    return int(number) ** 2

while True:
    line = sys.stdin.readline().rstrip()

    if line == '0 0 0':
        break

    numbers = list(map(square, line.split(maxsplit=2)))
    maximum = max(numbers)
    if maximum * 2 == sum(numbers):
        print('right')
    else:
        print('wrong')
