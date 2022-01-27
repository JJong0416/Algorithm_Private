import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):

    hq = []
    heapq.heappush(hq,[0,start])
    distance[start] = 0

    while hq:
        weight, cur = heapq.heappop(hq)

        if distance[cur] < weight: # 지금 꺼낸 가중치가 지금까지의 거리보다 길다면
            continue

        for i in computer[cur]: # 컴퓨터 안에는 (경로, 비용)이 들어가 있다.
            cost = weight + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(hq,[cost,i[0]])


T = int(input())
st = []
for tc in range(1,T+1):
    n,d,c = map(int,input().split())
    computer = [[] for _ in range(n+1)]
    visited = [[] for _ in range(n+1)]
    distance = [int(1e9)] * (n+1)

    for _ in range(d):
        a, b, s = map(int,input().split())
        computer[b].append([a,s])
    dijkstra(c)

    cnt = 0
    ans = 0

    for a in distance:
        if a != int(1e9):
            cnt += 1
            ans = max(ans,a)

    st.append([cnt, ans])


for a in range(len(st)):
    print(f"{st[a][0]} {st[a][1]}")
