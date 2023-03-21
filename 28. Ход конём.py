n, m = map(int, input().split())
dp = []
for i in range(n+2):
    dp.append([0]*(m+2))
dp[0][1] = 1
for i in range(2, len(dp)):
    for j in range(2, len(dp[i])):
        dp[i][j] = dp[i-2][j-1] + dp[i-1][j-2]

print(dp[-1][-1])