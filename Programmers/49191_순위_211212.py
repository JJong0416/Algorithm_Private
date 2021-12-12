"""
from collections import deque

def bfs(start):
    dq = deque()
    dq.append(start)
    visit[start] += 1

    visited = [False] * (n+1) # 중복 방문 체크
    visited[start] = True

    while dq:
        v = dq.popleft()

        for a in graph[v]:
            if not visited[a]:
                dq.append(a)
                visit[a] += 1


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

results.sort(key = lambda x : x[0])

graph = [[] for _ in range(n+1)]
visit = [ 0 for _ in range(n+1)] # 방문처리하기
cnt = 0

for res in results:
    win, lose = res
    graph[win].append(lose)

for i in range(1,n+1):
    bfs(i)

for i in visit:
    if i >= 5:
        cnt += 1
"""
def solution(n, results):
    answer = 0
    win_dict, lose_dict = {}, {}

    for i in range(1, n + 1):
        win_dict[i] = set()
        lose_dict[i] = set()

    for win, lose in results:
        win_dict[win].add(lose)
        lose_dict[lose].add(win)

    for i in range(1, n + 1):
        for winner in lose_dict[i]:
            win_dict[winner].update(win_dict[i])
        for loser in win_dict[i]:
            lose_dict[loser].update(lose_dict[i])

    for i in range(1, n + 1):
        if len(win_dict[i]) + len(lose_dict[i]) == n - 1:
            answer += 1

    return answer
"""
너무 어렵게 생각한 문제. 문제가 주어진 문제를 생각해보자.
1. 선수X가 있을 때, X를 이긴 사람과 X에게 진 사람들을 합치면 n-1
2. X에게 진 사람은 X를 이긴 사람에게 반드시 진다
3. X를 이긴 사람들은 X에게 진 사람에겐 반드시 이긴다.

이걸 바탕으로 문제를 해결해보자.
"""