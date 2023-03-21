operations = input().split()
stack = []
for i in range(len(operations)):
    if operations[i].isdigit():
        stack.append(int(operations[i]))
    else:
        if operations[i] == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a+b)
        if operations[i] == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a-b)
        if operations[i] == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a*b)

print(stack.pop())