m = int(input())
n = int(input())
sections = []
for i in range(n):
    a,b = map(int, input().split())
    sections.append([a,b])

count = 0
for i in range(n):
    count += 1
    for j in range(i + 1, n):
        if j <= n and sections[i][0] <= sections[j][1] and sections[j][0] <= sections[i][1]:
            count -= 1
            break
print(count)




