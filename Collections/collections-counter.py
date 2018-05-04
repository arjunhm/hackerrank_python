from collections import Counter

x = int(input())
shoeCounter = Counter(list(map(int, input().split())))
n = int(input())
total = 0

for cust in range(n):
    size, price = map(int, input().split())
    if size in shoeCounter.keys() and shoeCounter[size] > 0:
        total += price

print(total)
