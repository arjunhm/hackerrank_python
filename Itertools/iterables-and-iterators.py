import itertools

n = int(input())
array = input().split()
k = int(input())
num, den = 0, 0

for comb in itertools.combinations(array, k):
    if 'a' in comb:
        num += 1
    den += 1

print(num / den)
