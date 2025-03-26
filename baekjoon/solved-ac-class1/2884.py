import sys

h, m = map(int, sys.stdin.readline().rstrip().split(maxsplit=1))

# if m >= 45:
#     m -= 45
# else:
#     m += 15
#     h = 23 if h == 0 else h-1

m -= 45
if m < 0:
    m += 60
    h -= 1
    if h < 0:
        h = 23

print(h, m)
