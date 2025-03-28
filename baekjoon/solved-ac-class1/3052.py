import sys

values = set()
for index in range(10):
    number = (int(sys.stdin.readline().rstrip())) % 42
    values.add(number)

print(len(values))
