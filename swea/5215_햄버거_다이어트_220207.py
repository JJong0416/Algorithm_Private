"""
1. dp or dfs
2. combination 사용 x => 숫자가 정해지지 않음.
3. dp로도 풀 수 있지만, dfs가 이 문제의 의도인 것 같아서 dfs로 푸는 게 좋을 것 같다.
"""

import sys
input = sys.stdin.readline

def dfs(idx, ingre, kal):
    global max_comb

    if kal > L: # 칼로리 넘어가거나 갯수가 넘어가면
        return

    max_comb = max(max_comb,ingre) # 최대값 저장

    if idx == N:
        return

    l_ingre, l_kal = foods[idx]
    dfs(idx+1, ingre + l_ingre, kal + l_kal) # 재료 사용했다면
    dfs(idx+1, ingre, kal) # 재료를 사용 안했다면

T = int(input())

for tc in range(1,T+1):
    N,L = map(int,input().split())

    foods = [list(map(int,input().split())) for _ in range(N)]
    max_comb = 0

    dfs(0,0,0)

    print("#{} {}".format(tc,max_comb))
