"""
from collections import deque

numbers = [11,7]
ans = []

for num in numbers:
    num = deque(bin(num))
    num.popleft() # 0b 삭제
    num.popleft() # 0b 삭제

    if "0" not in num:
        num.append("1")
        num[1] = "0"
        ans.append(int(''.join(num), 2))
    else:
        if num[-1] == "0":
            num[-1] = "1"
            ans.append(int(''.join(num), 2))

        else:
            for i in range(len(num)-1,-1,-1):
                if num[i] == "0":
                    num[i], num[i+1] = num[i+1], num[i]
                    ans.append(int(''.join(num), 2))
print(ans)
"""
# 풀긴 했지만, 모든 테케를 통과 X
def solution(numbers):
    ans = []

    for i in numbers:
        if i % 2 == 0:
            ans.append(i + 1)

        else:
            bin_num = str(format(i, 'b'))
            point = bin_num.rfind('01')

            if point == -1:
                bin_num = '10' + bin_num[1:]
                ans.append(int(bin_num, 2))

            else:
                bin_num = bin_num[:point] + '10' + bin_num[point + 2:]
                ans.append(int(bin_num, 2))
    return ans