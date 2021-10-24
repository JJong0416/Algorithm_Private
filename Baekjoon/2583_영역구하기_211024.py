from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(sx,sy):
    tot = 1
    visited = [ [False] * M for _ in range(N)]
    visited[sx][sy] = True
    dq = deque()
    dq.append((sx,sy))

    while dq:
        x,y = dq.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and data[nx][ny] == 0:
                dq.append((nx,ny))
                visited[nx][ny] = True
                data[nx][ny] = 1
                tot += 1
    return tot


N,M,K = map(int,input().split()) # 5,7
data = [[0] * M for _ in range(N)]
part = 0
lst = []

for k in range(K):
    x1,y1,x2,y2 = map(int,input().split()) # 아니 값 왜 이따구로 주는거야 도대체
    # 0 2 / 4 4 =>
    # 02 12 22 32 03 13 23 33
    for i in range(y1,y2):
        for j in range(x1,x2):
            data[i][j] = 1

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            ans = bfs(i,j)
            lst.append(ans)
            part += 1
lst.sort()
print(part)
for l in lst:
    print(l, end= ' ')