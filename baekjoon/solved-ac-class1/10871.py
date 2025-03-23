import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
print(' '.join(map(str, filter(lambda i : i < x, list(map(int, sys.stdin.readline().rstrip().split()))[0:n]))))
