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
        linked[i].extend(party) # party 그대로 넣는데, 첫번째 인덱스는 몇번째 인덱스인지 나타내기 떄문에
        linked[i].remove(i) # party를 넣고 자기 자신을 뺸다.

dq = copy.deepcopy(known_list)

while dq: # bfs
    cur_man = dq.popleft()

    for i in linked[cur_man]:
        if not visit[i]:
            dq.append(i)
            visit[i] = True
            known_list.append(i)

cnt = 0

for party in party_list:
    if not set(party) & set(known_list): # 여기 부분이 핵심, 두 리스트가 공통된게 없을 때!!!★
        cnt += 1

print(cnt)
