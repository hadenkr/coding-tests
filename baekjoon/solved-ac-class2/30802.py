import sys, math

n = int(sys.stdin.readline().rstrip())
s = [int(i) for i in sys.stdin.readline().rstrip().split()]
[t, p] = [int(i) for i in sys.stdin.readline().rstrip().split()]

x = sum([math.ceil(i / t) for i in s])
q = n // p
print(x)
print(q, n - (p * q))
