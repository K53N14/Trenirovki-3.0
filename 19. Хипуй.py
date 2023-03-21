N = int(input())
heap = []
for _ in range(N):
    command = input().split()
    command[0] = int(command[0])
    if command[0] == 0:
        heap.append(int(command[1]))
        i = len(heap) - 1
        while i > 0:
            if heap[i] > heap[(i-1)//2]:
                heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
                i = (i-1)//2
            else:
                break
    else:
        ans = heap[0]
        heap[0] = heap[-1]
        i = 0
        while i * 2 + 2 < len(heap):
            maxchild = i * 2 + 1
            if heap[i * 2 + 2] > heap[maxchild]:
                maxchild = i * 2 + 2
            if heap[i] < heap[maxchild]:
                heap[i], heap[maxchild] = heap[maxchild], heap[i]
                i = maxchild
            else:
                break
        heap.pop()
        print(ans)


