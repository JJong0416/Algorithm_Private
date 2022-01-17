import math
import re


def zin(num, q):
    rev_base = ''

    while num > 0:
        num, mod = divmod(num, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime_number(x):
    for a in range(2, int(math.sqrt(x)) + 1):
        if x % a == 0:
            return False
    return True


def solution(n, k):
    zero = zin(n, k)
    cnt, check = 0, ""
    prime = []

    zero = zin(n, k)

    for i in range(len(zero)):
        if zero[i] == "0":
            #number = re.sub(r'[^1-9]', '', check) 없어도 상관은 없는데, 특수 문자가 들어오는 걸 방지한다. 즉 숫
            prime.append(check)
            check = ""
            continue
        check += zero[i]

    if i == len(zero) - 1 and check != "":
        prime.append(check)

    for i in prime:
        if i != '1' and i != '' and is_prime_number(int(i)):
            cnt += 1

    return cnt

"""
카카오 시험 당일날 풀었는데 다시 못푸는 내 인생이 레전드..
사실 문제를 잘못 이해한 것 같다 0P, P0, 0P0을 나눠서 prime에 넣고 있었다.
그럴 필요 없으며, 마지막 if문은 011 처럼 잔여 데이터를 처리하기 위한 조건이다.

is_prime_number 함수랑 특정 진수로 바꾸는 알고리즘은 좀 공부해두면 좋을 것이다.
"""