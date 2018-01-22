t = int(input())

for case in range(t):
    n1 = int(input())
    a = set(map(int, input().strip().split()))
    n2 = int(input())
    b = set(map(int, input().strip().split()))

    if len(a.difference(b)) == 0:
        print(True)
    else:
        print(False)
