import sys

n = int(sys.stdin.readline().rstrip())
words = [sys.stdin.readline().rstrip()]
added = set()
new_word = None

def custom_compare(s1, s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) > len(s2):
        return 1
    elif s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0

def print_all():
    for word in words:
        print(word)

def custom_search(start, end):
    global new_word

    number_of_elements = end - start
    if number_of_elements == 1:
        compared = custom_compare(new_word, words[start])
        if compared <= 0:
            return start
        else:
            return start + 1
    
    pivot_idx = start + int((number_of_elements + 1) / 2)
    compared = custom_compare(new_word, words[pivot_idx])
    if compared == 0:
        return pivot_idx
    elif compared < 0:
        idx = custom_search(start, pivot_idx)
        return idx
    else:
        idx = custom_search(pivot_idx, end)
        return idx

def start():
    global new_word

    if n == 1:
        return
    
    new_word = sys.stdin.readline().rstrip()
    if new_word not in added:
        compared = custom_compare(new_word, words[0])
        if compared < 0:
            words.insert(0, new_word)
            added.add(new_word)
        elif compared > 0:
            words.append(new_word)
            added.add(new_word)

    if n == 2:
        return

    for _ in range(2, n):
        new_word = sys.stdin.readline().rstrip()
        if new_word in added:
            continue

        total_length = len(words)
        pivot_idx = int(total_length / 2)

        compared = custom_compare(new_word, words[pivot_idx])
        if compared < 0:
            idx = custom_search(0, pivot_idx)
            words.insert(idx, new_word)
            added.add(new_word)
        elif compared > 0:
            idx = custom_search(pivot_idx, total_length)
            words.insert(idx, new_word)
            added.add(new_word)

start()
print_all()
