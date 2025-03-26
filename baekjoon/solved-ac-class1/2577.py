import sys

numbers = []
for index in range(3):
    numbers.append(int(sys.stdin.readline().strip()))

text = str(numbers[0] * numbers[1] * numbers[2])

dictionary = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

for char in text:
    dictionary[char] += 1

for key in range(10):
    print(dictionary[str(key)])
