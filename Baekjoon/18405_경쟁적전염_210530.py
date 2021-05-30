from collections import deque

N,K = map(int,input().split())
board = []
virus = []

for i in range(N): # 이 부분을 수정 안해서 계속 TLE 떴음.
    board.append(list(map(int,input().split())))

    for j in range(N):
        if board[i][j] != 0:
            virus.append((board[i][j],i,j))

S,X,Y = map(int,input().split())

dx = [0,0,-1,1] # L,R,U,D
dy = [-1,1,0,0]

def bfs(s,x,y):
    dq = deque(virus)
    count = 0

    while dq:
        if count == s: # 시간초 체크.
            break

        for _ in range(len(dq)):
            prev,x,y = dq.popleft()

            for k in range(4):
                nx,ny = x + dx[k], y + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 0:
                        board[nx][ny] = board[x][y]
                        dq.append((board[nx][ny],nx,ny))
        count += 1

virus.sort()
bfs(S,X,Y)
print(board[X-1][Y-1])