import sys

for index in range(9):
    number = int(sys.stdin.readline().rstrip())
    if index == 0:
        max = (number, index+1)
    elif number > max[0]:
        max = (number, index+1)

print('{}\n{}'.format(max[0], max[1]))
