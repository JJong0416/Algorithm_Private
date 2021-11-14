import sys

input = sys.stdin.readline

for _ in range(int(input())):

    typing = input().strip()
    left, right = [], []

    for t in typing:
        if t == '<':
            if left:
                right.append(left.pop())
        elif t == '>':
            if right:
                left.append(right.pop())
        elif t == '-':
            if left:
                left.pop()
        else:
            left.append(t)
    left.extend(reversed(right))
    print(''.join(left))


"""
구현은 맞음. 하지만, TLE. 변행해서 생각해봐야함.
"""
# import sys
#
# input = sys.stdin.readline
#
# T = int(input())
#
# for tc in range(T):
#     lst = list(map(str,input()))
#     st = []
#     cursor = 0
#
#     for l in lst:
#         check = ord(l)
#
#
#         if l == "<":
#             if cursor <= 0:
#                 continue
#             else:
#                 cursor -= 1
#
#         elif l == ">":
#             if cursor == len(st):
#                 continue
#             else:
#                 cursor += 1
#         elif l == "-":
#             try:
#                 st.pop()
#             except:
#                 continue
#             cursor -= 1
#
#         else:
#             st.insert(cursor,l)
#             cursor += 1
#
#         # print("문자:{} 커서:{}, 스택:{}".format(l,cursor,st))
#     print(''.join(st))
