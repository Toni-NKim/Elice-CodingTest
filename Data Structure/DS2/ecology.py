from sys import stdin
from collections import defaultdict

def input():
    return stdin.readline().rstrip()

# 총 입력된 나무들 사이에서 각 나무가 차지하는 비율을 출력 -> 처음에 문제 이해를 못함... 미국 전역이라면서?
trees = defaultdict(int)
orderedTrees = []
cnt = 0

while True:
    t = input()

    # break out of the loop if input stops.
    if not t:
        break

    trees[t] += 1
    cnt += 1

_list = sorted(list(trees))

for i in range(len(_list)):
    percentage = trees[_list[i]] / cnt * 100
    # 정규표현식
    percentage = '%.4f' % percentage
    trees[_list[i]] = percentage

for i in range(len(_list)):
    print(_list[i], trees[_list[i]])

# took 696ms.

# Simpler solution found online:
import sys
from collections import defaultdict
f = sys.stdin.readline

count = 0
result = defaultdict(int)
while True:
    a = f().rstrip()
    if not a:
        break
    result[a] += 1
    count += 1

result = sorted(result.items())

for i in result:
    print("%s %.4f" % (i[0], i[1]*100/count))