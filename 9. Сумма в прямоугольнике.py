def countprefsum(matrix,n,m):
    prefsum = [[0]*m]
    for i in range(n - 1):
        prefsum.append([0]*m)
        for j in range(len(prefsum[i]) - 1):
            prefsum[i+1][j+1] = prefsum[i][j+1] + prefsum[i+1][j] - prefsum[i][j] + matrix[i][j]
    return prefsum
def findprefsum(prefsum, x1,y1,x2,y2):
    return prefsum[x2][y2] - prefsum[x1-1][y2] - prefsum[x2][y1-1] + prefsum[x1-1][y1-1]

n,m,k = map(int, input().split())
matrix = []
for i in range(n):
    matrixrow = list(map(int, input().split()))
    matrix.append(matrixrow)

prefsum = countprefsum(matrix, n+1, m+1)

for i in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    ans = findprefsum(prefsum, x1,y1,x2,y2)
    print(ans)

