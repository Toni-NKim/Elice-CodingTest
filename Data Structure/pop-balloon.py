from sys import stdin
from collections import deque

# initialize variables
seq = []
n = int(input())
nums = list(map(int, stdin.readline().rstrip().split()))

# put balloons in deque
# match balloons and index to pop
# zip method: zip(key_list, val_list)
# could use enumerate() instead of list comprehension
# could use tuples in list as well -> [(idx+1,memo) for idx,memo in enumerate(map(int,input().split()))]
balloons = deque([i + 1 for i in range(n)])
d = dict(zip(balloons, nums))

#
while len(balloons) != 0:
    key = balloons.popleft()
    seq.append(key)
    toPop = -d[key] + 1 if -d[key] < 0 else -d[key]
    balloons.rotate(toPop)

for n in seq:
    print(n, end=' ')

# took 88ms