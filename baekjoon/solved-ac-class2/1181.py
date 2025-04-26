import sys
import time

start = time.time()

input = sys.stdin.readline
n = int(input())
added = { input().rstrip() for _ in range(n) }
words = list(added)
words.sort(key=lambda x :(len(x), x))

sys.stdout.write('\n'.join(words))

end = time.time()
print(f"{(end - start)*1000:.5f} ms")
