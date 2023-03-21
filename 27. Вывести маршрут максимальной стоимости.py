n, m = map(int, input().split())
field = []
for _ in range(n):
    line = list(map(int, input().split()))
    field.append(line)

dp = []
prev = []
for i in range(n+1):
    dp.append([0]*(m+1))

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + field[i-1][j-1]

print(dp[n][m])

i = n
j = m
ans = []
while i > 0 and j > 0:
    if i == 1 and j == 1:
        break
    if dp[i][j] - field[i-1][j-1] == dp[i-1][j]:
        ans.append('D')
        i-=1
    elif dp[i][j] - field[i-1][j-1] == dp[i][j -1]:
        ans.append('R')
        j-=1

ans = ans[::-1]
print(' '.join(ans))



