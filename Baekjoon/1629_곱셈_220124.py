"""
문제 보자마자 TLE 터질 것을 예상. 일단 pypy랑 sys사용해 시간을 줄이면서,
dp로 하면 시간이 줄 것 같지 않은가? => 아 그런데 범위가 너무 크고, 그러한 수치계산의 변화가 시간제한안에 들 수 있을까?
=> 결론은 B-F도 시간초과로 터지고, DP도 시간초과로 터진다. 그렇다면 남은건 재귀형식이다.
"""
def power(a,b):
    if b == 1:
        return A % C
    else:
        tmp = power(a, b//2)

        if b & 1 == 0: #짝수
            return tmp * tmp % C

        else:
            return tmp * tmp * a % C

import sys
input = sys.stdin.readline

A,B,C = map(int,input().split())

print(power(A,B))