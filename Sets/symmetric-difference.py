m = int(input())
m_set = set(map(int, input().split()))
n = int(input())
n_set = set(map(int, input().split()))

res = set()
res.update(m_set.difference(n_set))
res.update(n_set.difference(m_set))

for x in res.sort():
    print(x)
