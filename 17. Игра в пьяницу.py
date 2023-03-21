firstplayer = list(map(int, input().split()))
secondplayer = list(map(int, input().split()))

back1 = len(firstplayer)
back2 = len(secondplayer)
front1 = front2 = 0
count = 0
while back1 - front1 != 0 and back2 - front2 != 0 and count <= 1000000:
    if (firstplayer[front1] == 0 and secondplayer[front2] == 9) or (firstplayer[front1] > secondplayer[front2] and not (firstplayer[front1] == 9 and secondplayer[front2] == 0)):
        firstplayer.append(firstplayer[front1])
        firstplayer.append(secondplayer[front2])
        front2 += 1
        front1 += 1
        back1 += 2
    elif firstplayer[front1] == secondplayer[front2]:
        firstplayer.append(firstplayer[front1])
        secondplayer.append(secondplayer[front2])
        front2 += 1
        front1 += 1
        back1 += 1
        back2 += 1
    else:
        secondplayer.append(firstplayer[front1])
        secondplayer.append(secondplayer[front2])
        front2 += 1
        front1 += 1
        back2 += 2
    count += 1

if back1 - front1 == 0:
    print(f'second {count}')
elif back2 - front2 == 0:
    print(f'first {count}')
else:
    print('botva')





