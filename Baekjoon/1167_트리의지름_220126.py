"""
DFS 시간복잡도 : O(V + E) / 이때, V는 정점, E는 간선의 개수
BFS 시간복잡도 : O(V^2) / 이때, V는 정점.
다익스트라 시간복잡도 : O(ElogV)

DFS 아니면 다익스트라로 풀어야 할 것 같다. 하지만 문제에서 요구하는건 다익스트라인 것 같기 떄문에
다익스트라로 푼다.
다익스트라 : 어떤 한 정점에서 가장 먼 곳의 정점은 가장 먼 두 정점 중 하나이다
이게 핵심이다. 꼭 알아두자
"""

import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start)) # 0은 거리, start는 vertax Number
    distance = [int(1e9)] * (V+1)
    distance[start] = 0

    while heap:
        cur_dis, cur_node = heapq.heappop(heap)
        if distance[cur_node] < cur_dis:
            continue

        for n, d in graph[cur_node]:
            next_dis = d + cur_dis

            if next_dis < distance[n]:
                distance[n] = next_dis
                heapq.heappush(heap, (next_dis, n))

    return distance

V = int(input())

# 저장 정보
graph = [[] for _ in range(V+1)]

for i in range(V):
    lst = list(map(int,input().split()))

    for j in range(1,len(lst)-1,2):
        graph[lst[0]].append([lst[j],lst[j+1]])

dis = dijkstra(1)
max_val = dis.index(max(dis[1::]))
dis = dijkstra(max_val)
max_dis2 = max(dis[1::])
print(max_dis2)

"""
알아야 하는 개념
1. 그래프의 지름은 어느 한 정점에서 가장 먼 정점과 그 정점에서 가장 먼 정점이 가장 길은 길이이다.
2. 다익스트라 구현 방법 다시 공부하기
"""