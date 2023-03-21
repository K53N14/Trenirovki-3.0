n = int(input())
purtime = [[0,0,0],[0,0,0],[0,0,0]]
maxvalue = 0
for _ in range(n):
    a,b,c = map(int, input().split())
    purtime.append([a,b,c])
    if max(a,b,c) > maxvalue:
        maxvalue = max(a,b,c)

purtime[0] = [maxvalue + 1,maxvalue + 1,maxvalue + 1]
purtime[1] = [maxvalue + 1,maxvalue + 1,maxvalue + 1]
purtime[2] = [maxvalue + 1,maxvalue + 1,maxvalue + 1]

dp = [0] * (len(purtime))

for i in range(3, len(purtime)):
    dp[i] = min(dp[i-1]+purtime[i][0],dp[i-2]+purtime[i-1][1],dp[i-3]+purtime[i-2][2])
print(dp[-1])
