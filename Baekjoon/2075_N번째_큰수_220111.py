import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    nums = list(map(int,input().split()))

    if not hq:
        for num in nums:
            heapq.heappush(hq,num)
    else:
        for num in nums:
            if hq[0] < num:
                heapq.heappush(hq,num)
                heapq.heappop(hq)
print(hq[0])

"""
1. 정렬을 해서 풀기
2. Heap 구조를 사용해 문제를 풀기

# 1. 정렬 풀이


for i in range(N):
    lst = list(map(int,input().split()))
    data.append(lst)
data = sum(data,[])
print(sorted(data)[-N])

=> 시간 초과가 아니고 메모리 초과!?
일단, 표에 적힌 수가 -10억 ~ +10억 범위이므로 기존의 배열을 사용하면
메모리 초과가 날 수밖에 없다. 물론 Python은 int형에 범위는 오버프로우 문제가 따로 없지만,
백준에서는 메모리 제한을 뒀기 때문에, TLE가 아닌 MLE가 난 것이다.


# 2. Heap 구조로 풀기
처음에는 Max-heap을 이용하여 큐를 N-1번 pop을 해서 N번째 큰 수를 구하는 방법으로 구현했으나
메모리 초과가 발생하였다.
그렇기에 Min_heap을 이용해 우선순위 큐의 길이를 N만큼만 유지하도록 하였다


배운 것 :
2차원 배열 -> 1차원 배열로 간단하게 바꾸는 법
=> data = sum(data,[])

"""