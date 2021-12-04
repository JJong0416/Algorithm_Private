from itertools import permutations
k = 80
dungeons = 	[[80,20],[50,40],[30,10]]
# result = 3
_max = -int(1e9)
combin = list(permutations(dungeons,len(dungeons)))

for comb in combin:
    check = k # 하나의 값 미리 넣기
    result = 0

    for i in range(len(comb)):
        if check >= comb[i][0]:
            check -= comb[i][1]
            result += 1
        else:
            continue
    _max = max(_max,result)

print(_max)
