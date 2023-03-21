queue = []
commands = []
front = 0
back = 0
with open('input.txt', 'r') as f:
    for line in f:
        commands.append(line.strip())
for command in commands:
    command = command.split()
    if command[0] == 'push':
        queue.append(int(command[1]))
        print('ok')
        back += 1
    if command[0] == 'pop':
        if back - front == 0:
            print('error')
        else:
            print(queue[front])
            front += 1
    if command[0] == 'front':
        if back - front == 0:
            print('error')
        else:
            print(queue[front])
    if command[0] == 'size':
        print(back - front)
    if command[0] == 'clear':
        queue = []
        front = 0
        back = 0
        print('ok')
    if command[0] == 'exit':
        print('bye')
        break


