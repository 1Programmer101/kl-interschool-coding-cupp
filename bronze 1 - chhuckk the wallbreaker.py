v = int(input())
n = int(input())
broken = 0

while True:
    if v >= n:
        broken += 1
        v = v - n
    if v < n:
        break

print(broken)
