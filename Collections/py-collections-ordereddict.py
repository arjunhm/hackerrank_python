from collections import OrderedDict

n = int(input())
item_dict = OrderedDict()

for i in range(n):
    query = input().split()
    name = " ".join(query[:-1])
    price = query[-1]

    if name in item_dict:
        item_dict[name] += int(price)
    else:
        item_dict[name] = int(price)

for x in item_dict:
    print(x, item_dict[x])
