import sys

number = int(sys.stdin.readline().rstrip())
for index in range(number):
    values = sys.stdin.readline().rstrip().split('X')
    dictionary = {}
    score = 0
    for length in filter(lambda value: value > 0, map(len, values)):
        if length in dictionary:
            local_score = dictionary[length]
        else:
            local_score = int(length * (length + 1) / 2)
            dictionary[length] = local_score
        
        score += local_score

    print(score)
