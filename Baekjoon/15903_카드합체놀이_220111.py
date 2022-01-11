"""
heap으로 풀 수 있는 근거를 말해라
1. 문제 조건에서 이 점수를 가장 작게 만드는 것이 놀이의 목표라고 했다. 즉, DP 아니면 정렬로 문제를 풀어가라는 소리다.
2. 해당 문제를 여러번 반복하는 것이기 때문에, DP가 아닌 정렬로 문제를 푸는 것이 좋을 것 같다.
3. 일반적인 정렬해서 풀기 + 힙 사용해서 풀기로 해보자
"""

# Heap을 이용한 문제풀이
import  sys
import heapq

input = sys.stdin.readline

N,M = map(int,input().split())
hq = list(map(int,input().split()))

heapq.heapify(hq)

for i in range(M):
    card1 = heapq.heappop(hq)
    card2 = heapq.heappop(hq)
    newCard = card1 + card2
    heapq.heappush(hq,newCard)
    heapq.heappush(hq,newCard)

print(sum(hq))

"""
# 정렬로 문제를 해결해도 Solve
import  sys

input = sys.stdin.readline

N,M = map(int,input().split())
hq = list(map(int,input().split()))
hq.sort(reverse=True)

for i in range(M):
    card1 = hq.pop()
    card2 = hq.pop()
    newCard = card1 + card2
    hq.append(newCard)
    hq.append(newCard)
    hq.sort(reverse=True)

print(sum(hq))

"""