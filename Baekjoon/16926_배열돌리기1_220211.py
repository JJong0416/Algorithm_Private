import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [1,0,-1,0] # 하 우 상 좌
dy = [0,1,0,-1]

def rotate():
    # 여기서 deepcopy 썻다가 터짐. deepcopy
    _board = [[] for _ in range(N)]
    for i in range(N):
        _board[i] = board[i][:]

    start_x, start_y, end_x, end_y = 0, 0, N - 1, M - 1

    for i in range(min(N, M) // 2):
        x = start_x
        y = start_y

        for d in range(4):
            while True:
                nx, ny = x + dx[d], y + dy[d]
                if start_x <= nx <= end_x and start_y <= ny <= end_y:
                    board[nx][ny] = _board[x][y]
                    x,y = nx, ny
                else: # 범위 벗어나면
                    break
        start_x += 1; start_y += 1; end_x -= 1; end_y -= 1

for _ in range(R):
    rotate()

for i in range(N):
    print(*board[i])

"""
deepcopy < for i in range(N): _board[i] = board[i][:] 이 더 빠른 이유: 블로그
https://velog.io/@emplam27/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%9D%98-%EA%B9%8A%EC%9D%80%EB%B3%B5%EC%82%AC%EB%8A%94-deepcopy%EA%B0%80-%EB%B9%A0%EB%A5%BC%EA%B9%8C-slicing%EC%9D%B4-%EB%B9%A0%EB%A5%BC%EA%B9%8C
"""
