n1 = int(input())
a = set(map(int, input().split()))
n2 = int(input())

for case in range(n2):
    query, length = list(map(int, input().split()))
    b = set(map(int, input().split()))

    eval("a.{}({})".format(query, b))

print(sum(a))
