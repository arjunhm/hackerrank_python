import itertools

query = input().split()
s = query[0]
k = int(query[1])

letters = [x for x in s]
letters.sort()


for perm in itertools.combinations_with_replacement(letters, k):
    print("".join(perm))
