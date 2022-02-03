from collections import deque
import copy

n, m = map(int, input().split())

known_list = deque(map(int, input().split()[1:]))
linked = {i: [] for i in range(1, n + 1)}
party_list = []

visit = [False] * (n+1)

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    party_list.append(party)

    for i in party:
        linked[i].extend(party)
        linked[i].remove(i)

dq = copy.deepcopy(known_list)

while dq:
    cur_man = dq.popleft()

    for i in linked[cur_man]:
        if not visit[i]:
            dq.append(i)
            visit[i] = True
            known_list.append(i)

cnt = 0

for party in party_list:

    print(party, known_list)
    print("----")
    if not set(party) & set(known_list):
        print("set 구간")
        print(party, known_list)
        print("----")
        cnt += 1

print(cnt)
