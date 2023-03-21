deque = [0] * 10
commands = []
front = len(deque) - 1
back = len(deque)
overflowcounter = 0
with open('input.txt', 'r') as f:
    for line in f:
        commands.append(line.strip())
for command in commands:
    command = command.split()
    if command[0] == 'push_front':
        deque[front] = int(command[1])
        front -= 1
        print('ok')
    if command[0] == 'push_back':
        deque.append(command[1])
        print('ok')
        back += 1
    if command[0] == 'pop_front':
        if back - front - 1 == 0:
            print('error')
        else:
            print(deque[front + 1])
            front += 1
    if command[0] == 'pop_back':
        if back - front - 1 == 0:
            print('error')
        else:
            print(deque[-1])
            deque.pop()
            back -= 1
    if command[0] == 'front':
        if back - front - 1== 0:
            print('error')
        else:
            print(deque[front + 1])
    if command[0] == 'back':
        if back - front - 1== 0:
            print('error')
        else:
            print(deque[-1])
    if command[0] == 'size':
        print(back - front - 1)
    if command[0] == 'clear':
        deque = [0] * 10
        front = len(deque) - 1
        back = len(deque)
        print('ok')
    if command[0] == 'exit':
        print('bye')
        break

    if front == -1:
        overflowcounter += 1
        newdeck = [0] * (back - front - 1 + 10 * overflowcounter)
        for i in range(back - front - 1):
            newdeck[i + 10 * overflowcounter] = deque[front + 1 + i]
        deque = newdeck
        front = 10 * overflowcounter - 1
        back = len(newdeck)