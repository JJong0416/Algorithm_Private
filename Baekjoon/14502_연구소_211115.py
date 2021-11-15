import copy
from itertools import combinations
from collections import deque

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(sx,sy):
    count = 1
    visited[sx][sy] = 1
    dq = deque()
    dq.append((sx,sy))

    while dq:
        x,y = dq.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1 and tmp[nx][ny] != 1:
                count += 1
                visited[nx][ny] = 1
                tmp[nx][ny] = 2
                dq.append((nx,ny))

    return count

N,M = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(N)]
space = []
virus = []
ans = -int(1e9)
wallCount = 0

for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            space.append((i,j)) # 빈 공간 찾기

        elif data[i][j] == 1:
            wallCount += 1

        else:
            virus.append((i,j))

walls = list(combinations(space,3)) # 3개로 벽 세우는 경우의 수

for wall in walls:
    virusCount = 0

    tmp = copy.deepcopy(data)
    w1,w2,w3 = wall
    tmp[w1[0]][w1[1]] = 1
    tmp[w2[0]][w2[1]] = 1
    tmp[w3[0]][w3[1]] = 1

    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2 and visited[i][j] == 0:
                virusCount += bfs(i,j)

    ans = max(ans,(N*M)-(wallCount+3) - virusCount)

print(ans)

