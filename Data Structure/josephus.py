from collections import deque 

# initialize variables
dq = deque()
n, k = map(int, input().split())
result = []

# insert items into deque
for i in range(1, n + 1):
    dq.append(i)

while len(dq) > 0:
    dq.rotate(-k + 1)
    result.append(dq.popleft())

# set output according to the given example (<3, 6, 2, 7, 5, 1, 4>)
answer = ", ".join(map(str, result))
print(f"<{answer}>")

