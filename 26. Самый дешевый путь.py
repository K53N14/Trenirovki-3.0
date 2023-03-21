## max value == 20 * 20 * 100 +1
n, m = map(int, input().split())
field = []
maxvalue = 0
for _ in range(n):
    line = list(map(int, input().split()))
    field.append(line)

dp = []
prev = []
for i in range(n+1):
    dp.append([0]*(m+1))
for i in range(2, m+1):
    dp[0][i] = -1
for i in range(2, n+1):
    dp[i][0] = -1
for i in range(1,n+1):
    for j in range(1,m+1):
        if dp[i-1][j] == -1:
            dp[i][j] = dp[i][j - 1] + field[i - 1][j - 1]
        elif dp[i][j-1] == -1:
            dp[i][j] = dp[i - 1][j] + field[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + field[i-1][j-1]

print(dp[n][m])




