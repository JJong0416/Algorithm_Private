from collections import deque


def solution(n, computers):
    def bfs(start):
        dq = deque()
        dq.append(start)

        while dq:
            v = dq.popleft()

            for d in data[v]:
                if not visited[d]:
                    dq.append(d)
                    visited[d] = True

    data = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    cnt = 0

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] != 0 and i != j:
                data[i + 1].append(j + 1)

    for i in range(n):
        if not visited[i + 1]:
            visited[i + 1] = True
            bfs(i + 1)
            cnt += 1
    return cnt


"""
★핵심 1.
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] 을
data = [[], [2], [1], []] 으로 변환시켜주는 것이 핵심이다.

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] != 0 and i != j:
                data[i + 1].append(j + 1)
                
"""