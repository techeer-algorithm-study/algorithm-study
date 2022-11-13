m = int(input())
lst = []
start_num = 1
stack = []
answer = []

for i in range(m):
    n = int(input())
    lst.append(n)

for j in range(len(lst)):
    if start_num <= lst[j]:
        while start_num <= lst[j]:
            stack.append(start_num)
            start_num += 1
            answer.append("+")
        stack.pop()
        answer.append("-")
    else:
        last_num = stack[-1]
        stack.pop()
        if last_num > lst[j]:
            print("NO")
        else:
            answer.append("-")

# print(stack)
print(answer)
