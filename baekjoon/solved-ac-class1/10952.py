import sys

while(True):
    line = sys.stdin.readline().rstrip()
    if line != '0 0':
        print(sum(map(int, line.split(maxsplit=2))))
    else:
        break
    