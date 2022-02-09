"""
예전에 풀어본 문제.
범위 자체가 loop 2개를 돌리면 안되는 구조이다. 그렇기에 stack을 사용해보자.
"""

import sys
# input = sys.stdin.readline

N = int(input())
top = list(map(int,input().split()))
st = []
record = [0] * N

for i in range(len(top)):
    check = top[i]

    while st and top[st[-1]] < check:
        st.pop()

    if st:
        record[i] = st[-1] + 1 # 인덱스 조정

    st.append(i)

for i in record:
    print(i, end= ' ')