def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)

n, m = map(int, input().split())
vertices = []
for i in range(n+1):
    vertices.append([])
for _ in range(m):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

visited = [False] * (n+1)
dfs(vertices, visited, 1)
ans = []
count = 0
for i in range(1, len(visited)):
    if visited[i] == True:
        count += 1
        ans.append(i)

print(count)
ans = [str(x) for x in ans]
print(' '.join(ans))

