import sys

n, x = map(int, sys.stdin.readline().rstrip().split())

for i, y in enumerate(map(int, sys.stdin.readline().rstrip().split())):
    if i >= n:
        break
    elif y < x:
        print(y, end=' ')
