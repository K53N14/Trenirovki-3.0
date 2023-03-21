n = int(input())
coords = list(map(int, input().split()))
coords.sort()
if n < 3:
    print(coords[-1] - coords[0])
else:
    dp = [0] * n
    dp[0] = 0
    dp[1] = coords[1] - coords[0]
    dp[2] = coords[2] - coords[0]
    for i in range(3, n):
        dp[i] = coords[i] - coords[i-1] + min(dp[i-2], dp[i-1])

    print(dp[-1])
