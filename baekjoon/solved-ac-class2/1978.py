import math, sys

n = int(sys.stdin.readline().rstrip())
numbers = [int(i) for i in sys.stdin.readline().rstrip().split(maxsplit=n)[:n]]

dictionary = {}
count = 0

for i in numbers:
    if i == 2:
        count += 1
        continue
    if i == 1 or i % 2 == 0:
        continue

    is_prime = dictionary.get(i)
    if is_prime == True:
        count += 1
        continue
    if is_prime == False:
        continue

    value = math.floor(math.sqrt(i))
    if value == 1:
        dictionary[i] = True
        count += 1
    else:
        is_prime = True
        for j in range(2, value+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            dictionary[i] = True
            count += 1
        else:
            dictionary[i] = False

print(count)
