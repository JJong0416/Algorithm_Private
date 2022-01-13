import sys
from collections import  deque
input = sys.stdin.readline

def bfs(s):
    dq = deque()
    dq.append(s) #
    visited[s] = True

    while dq:
        x = dq.popleft()
        # for idx, item in enumerate(city[x]):
        #     if item and not visited[idx]:
        #         dq.append(idx)
        #         visited[idx] = True
        # 만약 enumerate를 쓰지 않고는?
        # =>

        for a in range(len(city[x])):
            if city[x][a] == 1 and not visited[a]:
                dq.append(a)
                visited[a] = True

N = int(input())
M = int(input())
city = [] # 인접행렬
visited = [False for _ in range(N)]

for _ in range(N):
    city.append(list(map(int, input().split())))

check = list(map(int,input().split()))

start = check[0]-1
bfs(start)
flag = True

for i in check:
    if not visited[i-1]:
        flag = False

if flag:
    print("YES")
else:
    print("NO")

"""
BFS를 인접 행렬로 문제를 풀어보는건 또 처음이다. 방식에 대해서 알아야 하는데, 
이때 Enumerate를 사용해 인접 행렬을 다 조사했다
for idx, item in enumerate(city[x]):
"""