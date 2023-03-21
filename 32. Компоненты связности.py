def dfs(graph, visited, now, comp):
    if visited[now] == 0:
        visited[now] = comp
        for neig in graph[now]:
            if not visited[neig]:
                dfs(graph, visited, neig, comp)


n, m = map(int, input().split())
vertices = []
for i in range(n+1):
    vertices.append([])
for _ in range(m):
    a, b = map(int, input().split())
    vertices[a].append(b)
    vertices[b].append(a)

visited = [0] * (n+1)
for i in range(len(vertices)):
    dfs(vertices, visited, i, i)

vertset = set(visited)
print(len(vertset)-1)
vertset = list(vertset)
vertset.sort()
for i in range(1,len(vertset)):
    ans = []
    count = 0
    for j in range(len(visited)):
        if visited[j] == vertset[i]:
            count += 1
            ans.append(j)
    print(count)
    ans = [str(x) for x in ans]
    print(' '.join(ans))