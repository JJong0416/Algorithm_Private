import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []
tot = 0
for i in range(N):
    heapq.heappush(hq,int(input()))

for i in range(N-1):
    card1, card2 = heapq.heappop(hq), heapq.heappop(hq)
    newCard = card1 + card2
    heapq.heappush(hq,newCard)
    tot += newCard

print(tot)

"""
10 20 30 40

# 순서대로 => 최소
=> (10 + 20) + (30 + 30) + (60 + 40) => 190

# 역순서 => 최대
=> (40 + 30) + (70 + 20) + (90 + 10) => 100 + 90 + 70 = 260

# 양 끝에서부터
=> (40 + 10) + (50 + 30) + (80 + 20) => 100 + 80 + 50 = 230

즉, 최소값들을 끊임없이 더하면서 전체 값을 계산해 나가는 것이 가장 작은 경우이다.
그렇기에, 최소값을 넣으면서 진행할 수 있어야 하기 때문에 priority Queue를 사용하면
시간복잡도에서 큰 이득을 볼 것이라고 생각이 든다.
"""
