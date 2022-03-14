import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]  # 동 남 서 북

N = int(input())
move_type = int(input())
ans = [[0] * N for _ in range(N)]

class Snall:
    def __init__(self, x, y, dc) -> None:
        self.x = x
        self.y = y
        self.dc = dc
        self.num = 1
        ans[x][y] = 1

    def move(self):
        # 이동할 수 있으면 흔적을 남기고 True 리턴
        # 이동할 수 없으면 한번 더 방향 바꿔서 체크하고, 그것도 이동이 안된다면 False 리턴
        nx, ny = self.x + dx[self.dc], self.y + dy[self.dc]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
            self.dc = (self.dc + 1) % 4

            nx, ny = self.x + dx[self.dc], self.y + dy[self.dc]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or ans[nx][ny] != 0:
                 return False
        self.x, self.y = nx, ny
        self.num += 1
        ans[nx][ny] = self.num
        return True

snails = [Snall(0, 0, 0), Snall(0, N - 1, 1), Snall(N - 1, N - 1, 2), Snall(N - 1, 0, 3)]

while True: # 뱀들이 한번에 한칸씩만 가게 하는 것
    flag = False
    for snail in snails:
        flag = snail.move()
    if not flag:
        break

if move_type == 0:
    temp = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[i][j] = ans[j][i]
    ans = temp

for i in range(N):
    for j in range(N):
        print(ans[i][j], end=' ')
    print()