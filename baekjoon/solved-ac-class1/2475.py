import sys

print(sum([int(str)**2 for str in sys.stdin.readline().rstrip().split(maxsplit=4)])%10)