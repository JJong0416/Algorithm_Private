from collections import deque

def solution(priorities, location):
    dq = deque()
    ans = []
    target = priorities[location]

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
        if ans[i][0] == location:
            return i+1
