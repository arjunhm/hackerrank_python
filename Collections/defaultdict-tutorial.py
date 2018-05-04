from collections import defaultdict

n, m = map(int, input().split())
word_dict = defaultdict(list)

for i in range(n):
    word_dict.setdefault(input(), []).append(str(i + 1))


for i in range(m):
    word = input()
    if word in word_dict:
        print(" ".join(word_dict[word]))
    else:
        print(-1)
