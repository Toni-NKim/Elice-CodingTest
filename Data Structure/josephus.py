from collections import deque 

# initialize variables
dq = deque()
n, k = map(int, input().split())
result = []

# insert items into deque
for i in range(1, n + 1):
    dq.append(i)

# deque.rotate() rotates to the right which means that rotate(k) will produce [5, 6, 7, 1, 2, 3, 4]
# To rotate to the left, put in a negative value.
# To pop from the left, has to rotate -k + 1
while len(dq) > 0:
    dq.rotate(-k + 1)
    print(dq)
    result.append(dq.popleft())

# set output according to the given example (<3, 6, 2, 7, 5, 1, 4>)
# join cannot iterate through int instances, has to convert to string
answer = ", ".join(map(str, result))
print(f"<{answer}>")

