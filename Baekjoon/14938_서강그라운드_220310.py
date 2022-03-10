import heapq, sys
input = sys.stdin.readline

def dijkstra(S):

    hq = []
    distance = [int(1e9)] * (N+1)

    heapq.heappush(hq, [0, S])
    distance[S] = 0

    while hq:
        now_dist, now_vertex = heapq.heappop(hq)

        if distance[now_vertex] < now_dist:
            continue

        for next_dist, next_vertex in board[now_vertex]:
            if next_dist + now_dist < distance[next_vertex]:
                next_dist += now_dist
                distance[next_vertex] = next_dist
                heapq.heappush(hq, [next_dist, next_vertex])

    return distance

N, M, R = map(int, input().split())

items = [0]+ list(map(int, input().split()))
board = [[] for _ in range(N + 1)]
_max = int(-1e9)

for _ in range(R): # 경로 설정
    start, end, dist = map(int, input().split())

    board[start].append([dist, end])
    board[end].append([dist, start])


for i in range(1, N+1):
    temp_sum = 0
    result = dijkstra(i)

    for j in range(1,N+1):
        if result[j] <= M:
            temp_sum += items[j]

    _max = max(_max, temp_sum)

print(_max)