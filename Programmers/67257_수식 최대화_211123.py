# from itertools import permutations
#
# def calc(operation,seq,exp):
#     if exp.isdigit(): # 더이상 exp에 연산자 없으면
#         return str(exp) # 숫자 그대로 리턴
#
#     else:
#         # print(exp)
#         if operation[seq] == "*":
#             split = exp.split("*") # 연산자로 쪼개고
#             tmp = []
#
#             for s in split:
#                 tmp.append(calc(operation,seq+1,s))
#             print(tmp)
#             return str(eval("*".join(tmp)))
#
#
#         if operation[seq] == "+":
#             split = exp.split("+")
#             temp = []
#             for s in split:
#                 temp.append(calc(operation, seq + 1, s))
#             return str(eval("+".join(temp)))
#
#         if operation[seq] == "-":
#             split = exp.split("-")
#             temp = []
#             for s in split:
#                 temp.append(calc(operation, seq + 1, s))
#
#             return str(eval("-".join(temp)))
#
#
# expression = "100-200*300-500+20"
# priorties = ["+", "-", "*"]
# priorties = list(permutations(priorties,3))
#
# check = []
# ans = 0
#
# for oper in priorties:
#     result = abs(int(calc(oper,0,expression)))
#     ans = max(ans,result)
#
# print(ans)

# 연산자의 우선순위를 재정의하여 만들수있는 절댓값이 가장 큰 숫자
# 주어지는 숫자는 모두 양수

from itertools import permutations
from collections import deque

expression = "100-200*300-500+20"
answer = 0

# 0. 숫자와 연산자로 분리

number = ''
op = set()
q = deque([])
for i in expression:
    if i.isdigit():
        number += i
    else:
        q.append(number)
        q.append(i)
        op.add(i)
        number = ''
q.append(number)
# q = deque(['100', '-', '200', '*', '300', '-', '500', '+', '20'])
print(op)
# 1. 주어진 문자열에 수식이 몇개있는지 확인
len_op = len(op)
op = list(op)
# 2. 수식의 가능한 우선순위를 모두 구한다.
for case in permutations(op, len_op):  # permutataion

    # 3. 해당 우선순위대로 계산했을때 나온 값들을 이전계산값과 비교하여 더큰값으로 계쏙 저장한다.
    new_q = deque([])
    _q = q.copy()  # 새로운 우선순위가 나오면 새롭게 계산해야 하므로 복사해주어야함

    # 3.1. 하나의 연산자마다 전체식을 한번 돌아서 새로운 식을 만든다고 생각
    for i in range(len_op): # 3
        # 큐가 빌때까지
        # q = deque(['100', '-', '200', '*', '300', '-', '500', '+', '20'])
        while _q:
            curr = _q.popleft()
            # 현재 우선순위에 해당하는 연산자라면
            if curr == case[i]:
                before = new_q.pop()
                after = _q.popleft()
                value = str(eval(before + case[i] + after))
                new_q.append(value)
            else:
                new_q.append(curr)

            print(new_q)
        # 현재 case에 대해 계산이 모두 완료된경우 최대값을 비교하여 갱신
        if len(new_q) == 1:
            answer = max(answer, abs(int(new_q[-1])))
            break
        _q = new_q.copy()  # 대상이 되는 큐를 새로운 식으로 바꿔준다. 이떄도 꼭 copy를 해줘야함
        new_q = deque([])  # 위에서 copy를 안하면 이게 반영이됨, 새로운 식을 저장할 공간 초기화
print(answer)

