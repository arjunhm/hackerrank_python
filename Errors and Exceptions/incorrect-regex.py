import re

t = int(input())

for case in range(t):

    try:
        re.compile(input())
        flag = True
    except re.error:
        flag = False

    print(flag)
