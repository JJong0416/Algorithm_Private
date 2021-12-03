# 초기 풀이 : Pass
# But, 코드가 너무 길고 불필요한 loop가 많음.
"""
def solution(genres, plays):
    table = {}
    rank = []
    result = []

    tmp = set(genres)

    for i in tmp:
        table[i] = []

    for i in range(len(plays)):
        play = plays[i]
        genre = genres[i]
        table[genre].append((play, i))

    for key, val in table.items():
        val.sort(key=lambda x: (-x[0], x[1]))

    for key, val in table.items():
        check = 0

        for i in val:
            check += i[0]
        rank.append((key, check))
    rank = sorted(rank, key=lambda x: -x[1])

    for r in range(len(rank)):
        key = rank[r][0]
        a = 0
        for i in table[key]:
            a += 1
            result.append(i[1])

            if a == 2:
                break
    return result
"""

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

answer = []
dic = {}

for i in range(len(genres)):
    if genres[i] in dic:
        # 현재 장르가 이미 dic에 있다면 그 장르에 해당하는 value의 0번째 index에 현재 index를 append해주고
        # 1번째 index에 재생횟수를 추가해준다.
        dic[genres[i]][0].append(i)
        dic[genres[i]][1] += plays[i]
    else:
        # 현재 장르가 dic에 없다면 dic에 현재 index와 재생횟수를 추가해준다.
        dic[genres[i]] = [[i], plays[i]]
print(dic.items())
""" 이 부분이 핵심인 것 같다. 여기서 dic.items()를 출력해 몇번째 배열인지 체크 후, sort 떄리면 빠르게 처리할 수 있을 것 같다."""

# dic.items()를 재생횟수순으로 내림차순 정렬(-x[1][1])해서 diclist에 할당한다.
diclist = sorted(dic.items(), key=lambda x: -x[1][1])
print(diclist)

#
# for i in diclist:
#     # 현재 장르에 속한 곡이 하나라면 하나만 answer에 추가시켜준다.
#     if len(dic[i[0]][0]) == 1:
#         answer.append(dic[i[0]][0][0])
#     else:
#         # 현재 장르에 속한 곡이 2개 이상이라면, 재생횟수순으로 내림차순 정렬한 뒤 상위 2개의 곡만 answer에 extend해준다.
#         dic[i[0]][0].sort(key=lambda x: -plays[x])
#         answer.extend(dic[i[0]][0][:2])
# print(answer)