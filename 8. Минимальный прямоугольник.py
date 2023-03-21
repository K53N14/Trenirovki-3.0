k = int(input())
xs = []
ys = []
for _ in range(k):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

print(min(xs), min(ys), max(xs), max(ys))
