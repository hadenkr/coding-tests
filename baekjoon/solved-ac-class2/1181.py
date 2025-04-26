import io, sys
import time

start = time.time()

lines = sys.stdin.readlines()
n = int(lines[0])
added = set(lines[1:n+1])
# added.remove(lines[0])
words = list(added)
words.sort(key=lambda x :(len(x), x))

buffer = io.StringIO()
for word in words:
    buffer.write(f'{word.rstrip()}\n')

print(buffer.getvalue().rstrip())

end = time.time()
print(f"{(end - start)*1000:.5f} ms")
