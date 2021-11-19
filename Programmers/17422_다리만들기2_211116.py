from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    global isl_num

    dq = deque()
    dq.append((x, y))
    isl_num_map[x][y] = isl_num
    while dq:
        x, y = dq.popleft()
        for z in range(4):
            nx, ny = x + dx[z], y + dy[z]
            if 0 <= nx < n and 0 <= ny < m and isl_num_map[nx][ny] == -1 and a[nx][ny]:
                isl_num_map[nx][ny] = isl_num
                dq.append((nx, ny))


def dfs(x, y, dic, bridge_dis, start):
    nx, ny = x + dx[dic] , y + dy[dic]

    if not 0 <= nx < n or not 0 <= ny < m:
        return

    if a[nx][ny] == 1: # 땅을 발견했는데
        end = isl_num_map[nx][ny]

        if start == end:
            return

        if bridge_dis == 1: # 지금까지 걸어온 길이 1 이면 종료
            return

        else: # 그게 아니라면
            isl_min_dis[start][end] = min(bridge_dis, isl_min_dis[start][end])
            return

    bridge_dis += 1
    dfs(nx, ny, dic, bridge_dis, start)


def find_min(cnt, index, end):
    global min_ans
    if cnt == end:
        q = deque()
        c = [0 for _ in range(isl_num)]
        isl_cnt, bridge_length = 1, 0
        for i in range(isl_num):
            if not c[i]:
                q.append(i)
                c[i] = 1
                while q:
                    x = q.popleft()
                    for nx in i2i[x]:
                        if select[i2i_bridge[x][nx]] and not c[nx]:
                            c[nx] = 1
                            q.append(nx)
                            isl_cnt += 1
                            bridge_length += isl_min_dis[x][nx]

        if isl_cnt == isl_num:
            min_ans = min(min_ans, bridge_length)
        return

    for i in range(index, bridge_num):
        select[i] = 1
        find_min(cnt+1, i+1, end)
        select[i] = 0


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
isl_num_map = [[-1]*m for _ in range(n)]

isl_num = 0
for i in range(n):
    for j in range(m):
        if a[i][j] and isl_num_map[i][j] == -1:
            bfs(i, j)
            isl_num += 1

isl_min_dis = [[10]*isl_num for _ in range(isl_num)]

for i in range(n):
    for j in range(m):
        if a[i][j]:
            for k in range(4):
                dfs(i, j, k, 0, isl_num_map[i][j])

i2i_bridge = [[-1]*isl_num for _ in range(isl_num)]
i2i = [[] for _ in range(isl_num)]

bridge_num = 0
for i in range(isl_num-1):
    for j in range(i+1, isl_num):
        if isl_min_dis[i][j] < 10:
            i2i_bridge[i][j] = bridge_num
            i2i_bridge[j][i] = bridge_num
            i2i[i].append(j)
            i2i[j].append(i)
            bridge_num += 1

select = [0 for _ in range(bridge_num)]
if isl_num % 2 == 0:
    start = isl_num // 2
else:
    start = (isl_num // 2) + 1
min_ans = sys.maxsize
for i in range(start, bridge_num+1):
    find_min(0, 0, i)

if min_ans == sys.maxsize:
    print(-1)
else:
    print(min_ans)















# from collections import deque
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
# def bfs(sx,sy):
#     global land_count
#     check = []
#     land_count += 1
#
#     dq = deque()
#     dq.append((sx,sy))
#
#     while dq:
#         x,y = dq.popleft()
#
#         for d in range(4):
#             nx,ny = x + dx[d], y + dy[d]
#             if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 1:
#                 visited[nx][ny] = 1
#                 graph[nx][ny] = land_count
#                 dq.append((nx,ny))
#                 check.append((nx,ny))
#
#     land.append((check,land_count))
#
#
# N,M = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# land = []
# bridge = []
# land_count = 0
#
# for i in range(len(graph)):
#     for j in range(len(graph[0])):
#         if graph[i][j] == 1 and visited[i][j] != 1:
#             bfs(i,j)
#
# visitedLand = []
#
# for l in land:
#     start = l[1]
#     end = -1
#     for dic in range(4): # 총 방향 4개
#
#         d1, d2 = dx[dic], dy[dic]
#         tmp_bridge = []
#
#         for cord in l: # 땅의 모든 좌표들
#             x1,y1 = cord[0], cord[1]
#             tot = 0
#             flag = True
#
#             for r in range(10): # 맥시멈은 길이가 10이기 때문에
#                 x1,y1 = x1 + d1, y1 + d2
#
#                 if 0 <= x1 < N and 0 <= y1 < M:
#                     if graph[x1][y1] != 0:
#                         if (x1,y1) in land:
#
#                         flag = False
#                         break
#                     else:
#                         tot += 1
#                         tmp_bridge.append((x1,y1))
#
#             if flag:
#                 continue
#             elif tot == 0 or tot == 1:
#                 continue
#             else:
#                 bridge.append((tmp_bridge,tot))
#
