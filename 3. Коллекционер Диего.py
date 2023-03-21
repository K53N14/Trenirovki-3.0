def binsearch(l, r, seq, x):
    while l < r:
        m = (l + r)//2
        if seq[m] >= x:
            r = m
        else:
            l = m + 1
    if seq[l] < x:
        return l + 1
    else:
        return l


n = int(input())
stickers = list(map(int, input().split()))
k = int(input())
collec = list(map(int, input().split()))
stickset = set(stickers)
stickset = list(stickset)
stickset.sort()
if len(stickset) == 1:
    for i in range(k):
        if collec[i] > stickset[-1]:
            print(1)
        else:
            print(0)
elif len(stickers) == 0:
    for i in range(k):
        print(0)
else:
    for i in range(k):
        print(binsearch(0, len(stickset) - 1, stickset, collec[i]))
