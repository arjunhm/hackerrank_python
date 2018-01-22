n = int(input())
a = set(map(int, input().split()))
c = int(input())

for comm in range(c):
    query = input()

    if query == "pop":
        a.pop()
    else:
        query = query.split()
        ele = int(query[1])
        if query[0] == "remove":
            a.remove(ele)

        else:
            a.discard(ele)

print(sum(a))
