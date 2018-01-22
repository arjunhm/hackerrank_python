import itertools

k, m = map(int, input().split())
max_array = []

for i in range(k):
    query = list(map(int, input().split()))
    max_array.append(query[1:])
    
max_val = -1

for array in itertools.product(*max_array):
    max_val = max(sum(map(lambda x: x ** 2, array)) % m, max_val)

print(max_val)
