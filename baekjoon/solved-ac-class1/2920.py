import sys

values = list(map(int, sys.stdin.readline().rstrip().split(maxsplit=7)))

if values == [1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif values == [8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else:
    print('mixed')
