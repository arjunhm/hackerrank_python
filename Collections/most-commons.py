from collections import Counter

s = input()
cntr = Counter(s)

i = 0
for k, v in sorted(cntr.items(), key = lambda x:(-x[1], x[0])):
    if i == 3:
        break
    print(k, v)
    i += 1

