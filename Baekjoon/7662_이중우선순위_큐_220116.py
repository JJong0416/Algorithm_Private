import sys
import heapq

def sync(heap):
    while heap and ident[heap[0][1]] == 0:
        # 만약 heap에 데이터가 있으면서, 내가 가지고 있는 최대값 혹은 최소값이 반대 큐에서 삭제가 되었다면 자신의 큐에서도 삭제시킨다.
        heapq.heappop(heap) # 아~ 빠진 갯수만큼 반대 heap에도 ident를 알 필요 없이 횟수만큼만 빼면 되는군아

T = int(input())
input = sys.stdin.readline

for tc in range(1,T+1):
    times = int(input())
    min_hq = []
    max_hq = []
    ident = [0] * 1000000
    cnt = 0

    for t in range(times):
        cmd, num = input().split()
        num = int(num)
        print(min_hq,"/", max_hq,"/", t)

        if cmd =="I":
            heapq.heappush(min_hq,(num,t))
            heapq.heappush(max_hq,(num * -1,t))
            ident[t] = 1 # 해당 id에 값이 들어갔다를 체크

        else: # D일 경우,
            if num == 1:
                sync(max_hq)
                if max_hq:
                    ident[max_hq[0][1]] = 0
                    heapq.heappop(max_hq)
            elif num == -1:
                sync(min_hq)
                if min_hq:
                    ident[min_hq[0][1]] = 0
                    heapq.heappop(min_hq)
    sync(max_hq)
    sync(min_hq)

    if not max_hq:
        print("EMPTY")
    else:
        print(heapq.heappop(max_hq)[0] * -1, heapq.heappop(min_hq)[0])


"""
기준 이중 우선순위 큐로는 시간초과

import sys
import heapq

T = int(input())
input = sys.stdin.readline

for tc in range(1,T+1):
    times = int(input())
    min_hq = []
    max_hq = []

    for t in range(times):
        cmd, num = input().split()
        num = int(num)

        if cmd =="I":
            heapq.heappush(min_hq,num)
            heapq.heappush(max_hq,(num * -1,num))

        elif cmd == "D":
            if not max_hq or not min_hq:
                print("EMPTY")
                continue
            else:
                if num == 1:
                    max_val = heapq.heappop(max_hq)[1]
                    min_hq.remove(max_val)

                elif num == -1:
                    min_val = heapq.heappop(min_hq)
                    max_hq.remove((min_val * -1,min_val))
    if max_hq:
        print(heapq.heappop(max_hq)[1], heapq.heappop(min_hq))
        
해당 코드는 시간초과가 나온다. 프로그래머스 레벨3에서도 이렇게 풀었던 것 같은데..
아무래도 remove같은 내장함수를 사용했기에 시간초과가 나는 것 같다. 이 부분에서 코드를 수정하면 패스할 수 있을듯?

1
7
I -45
I 653
I -642
I 45
I 97
D 1
D 1
"""