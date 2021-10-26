# 메모리 초과 1
import heapq as hq

N = int(input())
nums = []

for _ in range(N):
    for j in list(map(int, input().split())):
        hq.heappush(nums, j)

print(hq.nlargest(N, nums)[-1])

# 메모리 초과 2
N = int(input())
q = []

for i in range(N):
    r = list(map(int, input().split()))
    for j in r:
        q.append(j)

q = sorted(q)
print(q[-N])

# 블로그 보고 따라한 메모리 초과 안 뜨는 법
import heapq as hq

N = int(input())
nums = []

for _ in range(N):
    for j in list(map(int, input().split())):
        hq.heappush(nums, j)
    while len(nums) > N:
        hq.heappop(nums)
print(hq.heappop(nums))
