
#  이 문제를 잘못이해하고 있었다, 청소기가 움직이는 게 아니라, 반시계 방향, 시계방향으로 먼지들이 움직이는 것이다.
import sys

input = sys.stdin.readline



def dust_flow():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if data[i][j] != 0 and data[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != -1:
                        tmp_arr[nx][ny] += data[i][j] // 5
                        tmp += data[i][j] // 5
                data[i][j] -= tmp

    for i in range(R):
        for j in range(C):
            data[i][j] += tmp_arr[i][j]

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        data[x][y], before = before, data[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 이동
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        data[x][y], before = before, data[x][y]
        x = nx
        y = ny

R, C, T = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(R)]

up, down = -1, -1

for a in range(R):
    if data[a][0] == -1:
        up = a
        down = a+1
        break

for _ in range(T):
    dust_flow()
    air_up()
    air_down()


ans = 0

for a in range(R):
    for b in range(C):
        if data[a][b] > 0:
            ans += data[a][b]

print(ans)