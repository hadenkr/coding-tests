import sys

number = int(sys.stdin.readline().rstrip())
line = sys.stdin.readline().rstrip()[0:number]
print(sum(map(int, line)))
