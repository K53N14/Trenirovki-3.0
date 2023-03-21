stack = []
commands = []
with open('input.txt', 'r') as f:
    for line in f:
        commands.append(line.strip())
for command in commands:
    command = command.split()
    if command[0] == 'push':
        stack.append(int(command[1]))
        print('ok')
    if command[0] == 'pop':
        if len(stack) == 0:
            print('error')
        else:
            print(stack[-1])
            stack.pop()
    if command[0] == 'back':
        if len(stack) == 0:
            print('error')
        else:
            print(stack[-1])
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'clear':
        stack = []
        print('ok')
    if command[0] == 'exit':
        print('bye')
        break

