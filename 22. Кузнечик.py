n, k = map(int, input().split())

dp = [0] * (n+k+1)
dp[k] = 1
for i in range(k + 1, n + k):
    for diff in range(1, k + 1):
        dp[i] += dp[i - diff]

print(dp[n + k - 1])
