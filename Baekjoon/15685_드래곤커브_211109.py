N = int(input())
data = [[0] * 101 for _ in range(101)]

di = {0: [0,1], 1 : [-1,0], 2 : [0,-1], 3 : [1,0]}

for _ in range(N):
    x,y,d,g = map(int,input().split())
    data[y][x] = 1
    curve_info = [d]

    for _ in range(g):
        for i in curve_info[::-1]:
            curve_info.append((i+1) % 4)
            # 다음세대 = reverse(지금 세대) + 1
            # 이 규칙성을 찾는게 핵심

    nx, ny = x, y

    for curve in curve_info:
        nx = nx + di[curve][1]
        ny = ny + di[curve][0]
        data[ny][nx] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if data[i][j] + data[i+1][j+1] + data[i][j+1] + data[i+1][j] == 4:
            cnt += 1

print(cnt)