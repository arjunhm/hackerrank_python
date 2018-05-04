from collections import OrderedDict

n = int(input())
word_dict = OrderedDict()
cnt = 0

for i in range(n):
    word = input()
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


print(len(word_dict.keys()))
print(" ".join(str(x) for x in word_dict.values()))
