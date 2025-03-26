import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().rstrip().split(maxsplit=2))
    room = (n - 1) // h + 1
    floor = n % h
    if floor == 0:
        floor = h
    print(floor * 100 + room)
