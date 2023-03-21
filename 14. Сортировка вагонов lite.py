def cantrain(train):
    def popstuff(num, stack):
        while len(stack) != 0:
            if stack[-1] < num:
                lastval = stack.pop()
            else:
                return lastval
        return lastval

    stack = []
    lastval = 0
    for i in range(len(train)):
        if lastval > train[i]:
            return 'NO'
        if len(stack) == 0:
            stack.append(train[i])
        else:
            if train[i] < stack[-1]:
                stack.append(train[i])
            else:
                lastval = popstuff(train[i], stack)
                stack.append(train[i])
    return 'YES'

N = int(input())
train = list(map(int, input().split()))
ans = cantrain(train)
print(ans)





