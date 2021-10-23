# 핵심 1. bfs
# 핵짐 2. bfs를 통해서 값 비교 하고 tot 저장해가며 들어가기
from collections import deque
from copy import deepcopy

def checkMap():
    global L,R

    for i in range(N):
        for j in range(N):
            for d in range(4):
                print()



def bfs(sx,sy):

    dq = deque()
    dq.append((sx,sy))
    cnt = 1
    tot = data[sx][sy]
    lst.append((sx,sy))

    while dq:
        x,y = dq.popleft()

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(data[nx][ny] - data[x][y]) <= R :
                cnt += 1
                tot += data[nx][ny]
                lst.append((nx,ny))
                visited[nx][ny] = True
                dq.append((nx,ny))
    return cnt, tot

dx = [0,0,-1,1]
dy = [-1,1,0,0]

N, L, R = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
tmp = deepcopy(data)
visited = [[False] * N for _ in range(N)]

for a in range(N):
    for b in range(N):
        if not visited[a][b]:
            lst = []
            visited[a][b] = True
            c,t = bfs(a,b)

            for l in lst:
                lx, ly = l
                tmp[lx][ly] = t // c

