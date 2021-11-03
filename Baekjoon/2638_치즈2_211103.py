from copy import deepcopy
from collections import deque
import sys

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def findChessze(sx,sy):
    dq = deque()
    dq.append((sx,sy))
    visited = [[0] * M for _ in range(N)]
    visited[sx][sy] = 1
    table = {} # 테이블에 값 넣고 2 이하 다 빼고 2 이상은 내비두고 나중에 처리하기.
    lst = []

    while dq:
        x,y = dq.popleft()

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1:
                if data[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
                else: # data[nx][ny] == 1:
                    if (nx,ny) not in table:
                        table[(nx,ny)] = 1
                    else:
                        table[(nx,ny)] += 1

    for key,value in table.items():
        if value >= 2:
            lst.append(key)

    return lst

def deleteCheeze():
    for x,y in _list:
        data[x][y] = 0




N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
time = 0

while True:
    _list = findChessze(0,0)
    if len(_list) == 0:
        print(time)
        break
    deleteCheeze()
    time += 1
