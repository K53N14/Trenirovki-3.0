n = int(input())
arr = list(map(int, input().split()))

last = n - 1
heaplast = (last - 1) //2

for i in range(heaplast, -1, -1):
    pos = i
    lastpos = len(arr)
    while pos * 2 + 1 < lastpos:
        if pos * 2 + 2 < lastpos:
            max_son_index = pos * 2 + 2
        else:
            max_son_index = pos * 2 + 1
        if arr[max_son_index] < arr[pos * 2 + 1]:
            max_son_index = pos * 2 + 1
        if arr[pos] < arr[max_son_index]:
            arr[pos], arr[max_son_index] = arr[max_son_index], arr[pos]
            pos = max_son_index
        else:
            break


while last > 0:
    arr[0], arr[last] = arr[last], arr[0]
    pos = 0
    while pos * 2 + 1 < last:
        if pos * 2 + 2 < last:
            max_son_index = pos * 2 + 2
        else:
            max_son_index = pos * 2 + 1
        if arr[max_son_index] < arr[pos * 2 + 1]:
            max_son_index = pos * 2 + 1
        if arr[pos] < arr[max_son_index]:
            arr[pos], arr[max_son_index] = arr[max_son_index], arr[pos]
            pos = max_son_index
        else:
            break
    last -= 1

arr = [str(x) for x in arr]
print(' '.join(arr))