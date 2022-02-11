import sys
# input = sys.stdin.readline

"""
굳이 앞에서 다 dfs 할 필요없이, 마지막 라인에서 2를 찾고 뒤로 돌아가서 x좌표 꺼내오면 끝
또한, 100x100이라 dfs는 부담스러울 수 밖에 없음. bfs로 해결
"""

for tc in range(1,11):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]

    find = board[99].index(2)
    x,y = 99, find
    visited = [[False] * 100 for _ in range(100)]

    while x != 0:
        visited[x][y] = True
        if y - 1 >= 0 and board[x][y-1] and not visited[x][y-1] :
            y -= 1
            continue
        elif y + 1 < 100 and board[x][y+1] and not visited[x][y+1]:
            y += 1
            continue
        else:
            x -= 1
    print("#{} {}".format(tc,y))