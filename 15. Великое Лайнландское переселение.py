n = int(input())
prices = list(map(int, input().split()))
stack = []
ans = [-1] * n
for i in range(len(prices)):
    if len(stack) == 0:
        stack.append((prices[i],i))
    else:
        if prices[i] < stack[-1][0]:
            while len(stack)!= 0 and prices[i] < stack[-1][0]:
                price, index = stack.pop()
                ans[index] = i
            stack.append((prices[i],i))
        else:
            stack.append((prices[i],i))

ans = [str(x) for x in ans]
print(' '.join(ans))

