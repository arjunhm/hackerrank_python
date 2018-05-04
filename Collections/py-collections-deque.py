from collections import deque

n = int(input())
array = deque()

for x in range(n):
    query = input()
    
    if query[:3] == "pop":
        eval("array.{}()".format(query))
    else:
        comm, ele = query.split()
        eval("array.{}({})".format(comm, int(ele)))

print(" ".join(str(x) for x in array))
        
