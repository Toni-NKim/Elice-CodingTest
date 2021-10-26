import heapq as hq
from sys import stdin

def input():
    return stdin.readline().rstrip()

# 가장 첫 번째 줄: 입력 데이터의 수 N
N = int(input())

for i in range(N):
    # 테스트 데이터 첫째 줄: 연산 개수 수 K
    K = int(input())
    # initialize Dual Priority Queue before each loop.
    minQ, maxQ = [], []
    for j in range(K):
        call = input().split()
        ins, num = call; num = int(num)
        # K -> 삭제 D or 입력 I 정수 n
        # 삭제 시 D 1은 최댓값 삭제, D -1은 최솟값 삭제
        if ins == 'I': 
            hq.heappush(minQ, num)
            hq.heappush(maxQ, -num)
        if ins == 'D': 
                if num -1:
                    hq.heappop(minQ)
                    hq.heappop(maxQ)
                else:
                     q.pop()
            else:
                pass

    if len(q) > 0:
        print(q[-1], q[0])
    else:
        print('EMPTY')