n = int(input())
quans  = []
for _ in range(n):
    quan = int(input())
    quans.append(quan)
ans = 0
for i in range(1,len(quans)):
    if quans[i] >= quans[i-1]:
        ans += quans[i-1]
    else:
        ans += quans[i]
print(ans)

