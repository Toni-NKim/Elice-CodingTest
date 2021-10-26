from collections import deque

# initialize variables
n = int(input())

# put cards in deque
cards = deque([i + 1 for i in range(n)])

while len(cards) != 1:
    # discard the card in front
    cards.popleft()
    # move the card next in line to the end
    cards.append(cards.popleft())

# print the card survived till the end
print(cards[0])

# took 288ms.