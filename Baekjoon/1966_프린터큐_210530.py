from collections import deque

T = int(input())

for tc in range(T):
    ans = []
    dq = deque()

    N,M = map(int,input().split())
    priorities = list(map(int,input().split()))

    for idx,val in enumerate(priorities):
        dq.append((idx,val))

    while dq:
        MAX = max(priorities)
        idx, val = dq.popleft()

        if val >= MAX:
            ans.append((idx,val))
            priorities[idx] = 0

        else:
            dq.append((idx,val))

    for i in range(len(ans)):
        if ans[i][0] == M:
            print(i+1)
