from sys import stdin
from collections import deque

# initialize variables
n = int(input())
dq = deque()

for i in range(n):
    # use .rstrip() to remove '\n'
    call = list(stdin.readline().rstrip().split())
    if len(call) > 1:
        ins, val = call
        if ins == "push": 
            dq.append(val)
    else:
        ins = call[0]
        # 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
        if ins == "pop": print(dq.popleft() if len(dq) != 0 else -1)
        # 큐에 들어있는 정수의 개수를 출력.
        if ins == "size": print(len(dq))
        # 큐가 비어있으면 1, 아니면 0을 출력.
        if ins == "empty": print(1 if len(dq) == 0 else 0)
        # 큐의 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
        if ins == "front": print(dq[0] if len(dq) != 0 else -1)
        # 큐의 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력.
        if ins == "back": print(dq[-1] if len(dq) != 0 else -1)


# took 2376ms.