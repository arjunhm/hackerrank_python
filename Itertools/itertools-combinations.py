import itertools

query = input().split()
s = query[0]
k = int(query[1])

letters = [x for x in s]
letters.sort()

for x in range(1, k + 1):
    for perm in itertools.combinations(letters, x):
        print("".join(perm))
