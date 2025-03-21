import sys

number = int(sys.stdin.readline().rstrip())
for index in range(number):
    values = sys.stdin.readline().rstrip().split(maxsplit=1)
    repeat = int(values[0])
    print(''.join([char * repeat for char in values[1]]))
