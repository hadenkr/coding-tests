import sys

for line in sys.stdin.readlines():
    print(sum(map(int, line.rstrip().split(maxsplit=2))))
