import itertools

a = list(map(int, input().split()))
b = list(map(int, input().split()))

string = ""
for x in itertools.product(a, b):
    string += str(x) + " "

print(string)
