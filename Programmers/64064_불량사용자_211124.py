
# 초기 풀이
"""from itertools import permutations, combinations, combinations_with_replacement, product

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

table = [[] for _ in range(len(banned_id))]

for i in range(len(banned_id)):
    ban = banned_id[i]

    for user in user_id:
        if len(user) != len(ban):
            continue

        for c in range(len(user)):
            if user[c] == ban[c]:
                if c == len(user)-1 :
                    table[i].append(user)
                else:
                    continue

            else:
                if ban[c] == "*":
                    if c == len(user) - 1:
                        table[i].append(user)
                    continue
                else:
                    break

lst = list(product(*table))

result = []
ret = 0
for l in lst:
    l = set(l)
    if len(l) == len(banned_id):
        result.append(''.join(l))

result = set(result)
print(len(result))"""

# 해결 풀이
from itertools import permutations
import re

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

from itertools import permutations
import re

answer = set()
n = len(banned_id) # 제재 아이디 개수
perm = list(permutations(user_id, n)) # user_id의 n개 원소로 순열 생성

for p in perm:
    cnt = 0 # 아이디가 일치하는지 확인

    for i in range(n):
        if not re.match(banned_id[i].replace('*', '.'), p[i]) or len(banned_id[i]) != len(p[i]):
            break
        else:
            cnt += 1 # p로 제재 아이디 목록은 만들 수 있음
        if cnt == n:
            answer.add(frozenset(p))
print(answer)
