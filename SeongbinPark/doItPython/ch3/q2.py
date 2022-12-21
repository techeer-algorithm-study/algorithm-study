n = input()
firstScores = list(map(int, input().split()))
M = max(firstScores)

newList = []
for i in firstScores:
    newList.append(int(i) / M * 100)
result = sum(newList)/int(n)

print(result)
