import heapq
import sys

input = sys.stdin.readline
leftHeap = [] # 중간 값보다 작은 수를 넣는 Heap  / 최대 힙으로 구현
rightHeap = []  # 중간 값보다 큰 수를 넣는 Heap / 최소 힙으로 구현
answer = []

N = int(input())

for i in range(N):

    x = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, (-x, x))
    else: # 두 개의 heap의 크기가 다를 경우 =>
        heapq.heappush(rightHeap, (x, x))

    if len(leftHeap) >= 1 and len(rightHeap) >= 1 and leftHeap[0][1] > rightHeap[0][1]:  # 루트값 비교,left힙 루트값이 rightHeap 루트값보다 보다 크다면,
        _min = heapq.heappop(rightHeap)[0] # rightHeap의 가장 작은 값 꺼내고,
        _max = heapq.heappop(leftHeap)[1] # leftHeap 가장 큰 값을 꺼내서
        heapq.heappush(leftHeap, (-_min,_min))
        heapq.heappush(rightHeap, (_max,_max))

    answer.append(leftHeap[0][1])

for i in answer:
    print(i)


"""
ex) 1,5,2,10,-99,7,5

left // right
 1       10
 2        5

"""


"""
1 1
5 1
2 2
10 2
- 99 => -99,1,2,5,10 => 2
7 => -99,1,2,5,7,10 => 2
5 => -99,1,2,5,5,7,10 => 5

어떻게 접근할 것인가?

1. left힙과 right힙에 
2. leftHeap과 rightHeap의 길이가 같다면 (즉, 두 heap에 들어있는 리스트 요소의 수가 같다면) 중간값의 기준이 되는
leaftheap에 수를 넣는다.


/* Brute-Force => TLE(Time Limit Exceeds) */
import sys

input = sys.stdin.readline
lst = []
N = int(input())
length = 0
for i in range(N):
    x = int(input())
    lst.append(x)
    lst.sort()
    length += 1

    if length % 2 == 0:
        check = length // 2 -1
        print(lst[check])
    else:
        check = length // 2
        print(lst[check])



"""