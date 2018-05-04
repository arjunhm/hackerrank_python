from collections import namedtuple

n = int(input())
col = input().split()
student = namedtuple('Student', col)
total = 0

for x in range(n):
    detail = input().split()
    student_tuple = student(detail[0], detail[1], detail[2], detail[3])
    total += int(student_tuple.MARKS)
    
print(total / n)
