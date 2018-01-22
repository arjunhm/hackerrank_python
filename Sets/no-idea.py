n, m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
h = 0

for x in array:
    if x in a:
        h += 1
    if x in b:
        h -= 1

print(h)
