s = input()
array = []

prev_val = s[0]
cnt = 1

if len(s) > 1:
    for x in range(1, len(s)):

        if s[x] == prev_val:
            cnt += 1
            
        else:
            array += [(cnt, int(prev_val))]
            cnt = 1
            prev_val = s[x]


    array += [(cnt, int(s[x]))]

else:
    print((1, int(s)))

for x in array:
    print(x, end = " ")
