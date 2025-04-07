import sys

line = sys.stdin.readline().rstrip()
dictionary = {}
for (index, char) in enumerate(line):
    if char not in dictionary:
        dictionary[char] = index

def get_index(ascii):
    return str(dictionary.get(chr(ascii), -1))

print(' '.join(list(map(get_index, range(97, 123)))))
