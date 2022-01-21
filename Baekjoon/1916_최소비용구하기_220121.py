"""
보자마자 다익스트라가 생각이 났다 근거에 대해서 말하자면,
1. 최소 비용
2. A -> B로 갈 때
3. N <= 1,000 , M <= 100,000

일단 최소 비용만 보면 BFS, DFS, Dijkstra가 떠올를 것이다.
그리고 A->B로 가면서 동시에 범위를 보면 N,M이 상당히 큰 수이다.
그렇기에 BFS로 시간이 초과할 수 있기 때문에 다익스트라로 푸는 것이 맞다고 생각했다.
"""
import sys
import heapq
input = sys.stdin.readline


def dijkstra(start):
    hq = [] # heapq 설정
    heapq.heappush(hq,(0,start))
    dist[start] = 0

    while hq:
        weight, now = heapq.heappop(hq)

        if dist[now] < weight:
            continue

        for a in data[now]:
            cost = weight + a[1]

            if cost < dist[a[0]]:
                dist[a[0]] = cost
                heapq.heappush(hq,(cost,a[0]))


n = int(input())
m = int(input())

data = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dist = [int(1e9)] * (n+1)

for i in range(m):
    s, d, w = map(int,input().split())
    data[s].append([d,w])

start, end = map(int,input().split())
dijkstra(start)
print(dist[end])