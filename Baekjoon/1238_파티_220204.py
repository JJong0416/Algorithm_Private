import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        dist, cur = heapq.heappop(hq)

        if distance[cur] < dist:
            continue

        for z in graph[cur]:
            cost = dist + z[1] # 비용

            if distance[z[0]] > cost:
                distance[z[0]] = cost
                heapq.heappush(hq,(cost,z[0]))

N, M, X = map(int,input().split())

graph = [[] for _ in range(N+1)]
max_dist = -int(1e9)

for i in range(M):
    sp,dp,move = map(int,input().split())
    graph[sp].append([dp,move])


for i in range(1,N+1):
    tot = 0
    distance = [int(1e9)] * (N + 1)
    dijkstra(i)
    tot += distance[X]

    distance = [int(1e9)] * (N + 1)
    dijkstra(X)
    tot += distance[i]
    max_dist = max(max_dist, tot)
print(max_dist)