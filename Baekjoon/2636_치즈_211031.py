from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def breakCheese(cheeze):
    time_lst.append(len(cheeze))

    for l in cheeze:
        x,y = l
        graph[x][y] = 0

def bfs(sx,sy):
    dq = deque()
    dq.append((sx,sy))
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1
    lst = set()

    while dq:
        x,y = dq.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                   dq.append((nx,ny))

                elif graph[nx][ny] == 1:
                    lst.add((nx,ny))
    if len(lst) == 0:
        return 0
    else:
        breakCheese(lst)
        return 1


N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
time_lst = []
time = 0

while True:
    check = bfs(0,0)

    if check == 0:
        break
    else:
        time += 1
print(time)
print(time_lst[-1])
