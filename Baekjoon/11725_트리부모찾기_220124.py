from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    dq = deque()
    dq.append(start)

    while dq:
        x = dq.popleft()

        for a in data[x]:
            if mother[a] == 0:
                mother[a] = x
                dq.append(a)
            else:
                continue

N = int(input())

data = [[] for _ in range(N+1)]
mother = [0 for _ in range(N+1)]

for i in range(N-1):
    s, e = map(int,input().split())
    data[s].append(e)
    data[e].append(s)

bfs(1)

for i in range(2,len(mother)):
    print(mother[i])
