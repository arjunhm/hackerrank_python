k = int(input())
rooms = list(map(int, input().split()))

room_set = set(rooms)

ans = sum(room_set) * k - sum(rooms)
ans = ans // (k - 1)
print(ans)


"""
Explanation

Let rooms = [1, 1, 1, 2, 2, 2, 3, 3, 3] where k = 3
room_set = [1, 2, 3] #distinct rooms

Now, sum(room_set) * k - sum(rooms) will be equal to 0
sum(room_set) = 6
sum(rooms) = 18
6 * 3 - 18 = 0

Now, rooms list has a number that occurs only once and that is the captain's room
Let rooms = [1, 1, 1, 2, 2, 2, 3, 3, 3, 8] where k = 3

sum(room_set) * k - sum(rooms) will be equal to 16
sum(room_set) = 14
sum(rooms) = 26
14 * 3 - 26 = 16
16 / (k - 1) => 16 / 2 = 8
"""
