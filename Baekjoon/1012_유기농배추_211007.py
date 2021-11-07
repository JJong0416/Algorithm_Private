from collections import deque
import sys

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(sx,sy):
    dq = deque()
    dq.append((sx,sy))

    while dq:
        x,y = dq.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and data[nx][ny] == 1:
                dq.append((nx,ny))
                visited[nx][ny] = 1
    return 1

T = int(input())
st = []

for tc in range(T):
    M,N,K = map(int,input().split())

    visited = [[0] * M for _ in range(N)]
    data = [[0] * M for _ in range(N)]
    count = 0

    for z in range(K):
        ax,ay = map(int,input().split())
        data[ay][ax] = 1


    for i in range(N):
        for j in range(M):
            if data[i][j] == 1 and visited[i][j] == 0: # 방문 안된거면서 동시에 data==1인 경우
                count += bfs(i,j)
    st.append(count)

for i in st:
    print(i)