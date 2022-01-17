def solution(id_list, report, k):
    table = {}
    pos = {}
    ans = [0 for _ in range(len(id_list))]

    for lst in range(len(id_list)):
        table[id_list[lst]] = set()
        pos[id_list[lst]] = lst

    for rep in report:
        a, b = rep.split()

        table[b].add(a)

    for idx, lst in table.items():
        if len(lst) >= k:
            for l in lst:
                ans[pos[l]] += 1

    return ans
"""
30분 걸림.. 이런 문제는 20분안에 해결했어야 헀는데...
table안에 lst들을 어떻게 순서대로 옮겨야하는지에 대해서 시간을 많이 뺏긴 것 같다.
이렇게 단순한건 pos 테이블 하나 더 만들어 위치를 알려주도록 한다.
"""