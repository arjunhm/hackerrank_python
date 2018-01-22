a = set(map(int, input().strip().split()))
n = int(input())

flag = False

for test in range(n):
    b = set(map(int, input().strip().split()))
    
    if len(b.difference(a)) == 0:
        flag = True
    else:
        flag = False
        break

print(flag)
