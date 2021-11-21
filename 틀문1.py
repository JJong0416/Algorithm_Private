
# https://www.daleseo.com/python-collections-defaultdict/
from collections import defaultdict

def solution(rows, columns, connections, queries):
    answer = []
    dict_list = defaultdict(dict) # 파이썬의 내장 자료구조인 dictionary가 value가 없는 경우 처리하는 방식
    print(dict_list.items())

    for r1,c1,r2,c2 in connections:
        dict_list[(r1,c1)][(r2,c2)] = 1
        dict_list[(r2,c2)][(r1,c1)] = 1

    print(list(dict_list))

    for query in queries:
        r1,c1,r2,c2 = query
        cnt = 0
        r1,r2 = min(r1,r2),max(r1,r2)
        c1,c2 = min(c1,c2),max(c1,c2) # 예외 처리를 위해서

        for y in range(c1,c2+1):
            if r1-1>=1:
                if dict_list[(r1,y)].get((r1-1,y)):
                    dict_list[(r1,y)][(r1-1,y)] = 0
                    dict_list[(r1-1,y)][(r1,y)] = 0
                    cnt += 1

            if r2+1<=rows:
                if dict_list[(r2,y)].get((r2+1,y)):
                    dict_list[(r2,y)][(r2+1,y)] = 0
                    dict_list[(r2+1,y)][(r2,y)] = 0
                    cnt += 1

        for x in range(r1,r2+1):
            if c1-1>=1:
                if dict_list[(x,c1)].get((x,c1-1)):
                    dict_list[(x,c1)][(x,c1-1)] = 0
                    dict_list[(x,c1-1)][(x,c1)] = 0
                    cnt += 1
            if c2+1<=columns:
                if dict_list[(x,c2)].get((x,c2+1)):
                    dict_list[(x,c2)][(x,c2+1)] = 0
                    dict_list[(x,c2+1)][(x,c2)] = 0
                    cnt += 1
        answer.append(cnt)
    return answer

solution(4, 3, [[1, 1, 2, 1], [1, 2, 1, 3], [1, 3, 2, 3], [2, 2, 2, 3], [2, 2, 3, 2],
                [2, 3, 3, 3], [3, 2, 3, 3], [3, 2, 4, 2], [4, 1, 4, 2]],
         [[2, 2, 3, 1], [1, 2, 4, 2]])