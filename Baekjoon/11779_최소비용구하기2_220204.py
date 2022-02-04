import sys
import heapq

input = sys.stdin.readline

def dijkstra(start):
    hq = []
    heapq.heappush(hq,(0,start))
    distance[start] = 0

    while hq:
        dist, cur = heapq.heappop(hq)

        if distance[cur] < dist:
            continue

        for next, nextDist in graph[cur]:
            cost = dist + nextDist

            if cost < distance[next]:
                distance[next] = cost
                nearnest[next] = cur # 기존 다익스트라에 추가된 부분!
                heapq.heappush(hq,(cost,next))

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for i in range(M):
    sp, dp, move = map(int,input().split())
    graph[sp].append((dp,move))

s, e = map(int,input().split())

distance = [int(1e9)] * (N+1)
nearnest = [s] * (N+1)

dijkstra(s)

ans = []
tmp = e # 도착지점

while tmp != s: # 스타트 부분 나오면 역순으로 다 도착했다는 뜻
    ans.append(str(tmp))
    tmp = nearnest[tmp]

ans.append(str(s))
ans.reverse()

print(distance[e])
print(len(ans))
print(" ".join(ans))



"""
https://ku-hug.tistory.com/130
다익스트라로 구현은 했지만, 마지막 노드까지의 거리를 bfs로 하다 시간초과가 터져 다른 방식을 찾음
나랑 푸는 스타일도 정말 비슷하지만, 그것보다 nearnest 방식이 정말로 참신하고
처음 보는 풀이기에 참고하면서 공부했다. 진짜 개고수인듯하다 이 사람은..
"""
