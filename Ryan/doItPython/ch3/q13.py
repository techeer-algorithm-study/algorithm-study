n = int(input())

cards = [i+1 for i in range(n)]

while len(cards) > 1:
    cards.pop(0)
    firstCard = cards[0]
    cards.append(firstCard)
    cards.pop(0)
print(cards[0])


# deque from collections handles pop(0)
# deque().popleft() = list.pop(0)