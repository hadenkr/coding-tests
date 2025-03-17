number = int(input())
for i in range(0, number):
    a, b = input().split(maxsplit=2)
    print(f'{int(a) + int(b)}')