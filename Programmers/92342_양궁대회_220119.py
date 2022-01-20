"""
풀기 전:
어떻게 풀어야 할 지 25분 넘게 고민했다 ㅋㅋㅋㅋ..
문제를 보자마자 생각났던 건 DP였는데, 발사하지 않은 부분과 발사하고 발사안한 부분 합쳐서 DP,
그리고 발사한 부분까지 DP로 하는건 점화식으로 해결할 수 없을 것 같아 Brute-force로 풀어야 한다고 생각.
배열의 길이는 11이고, 최악으론 11! = 39916800이므로 1억이 되지 않는 숫자이다.
Brute-force로 해결하기 위해 배열을 어떻게 담느냐가 중요한 것 같다.
"""
# 풀이 1
from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, comb_cnt = 0, {}

    for comb in combinations_with_replacement(range(11), n): # 0~11까지 n개의 조합. 대신 반복되는 요소가 있게 ex) "ABC",2 => AA, AB, AC, BB, BC ,CC
        cnt = Counter(comb)
        score1, score2 = 0, 0

        for i in range(1, 11):
            if info[10 - i] < cnt[i]:
                score1 += i
            elif info[10 - i] > 0:
                score2 += i

        diff = score1 - score2
        if diff > max_diff:
            comb_cnt = cnt
            max_diff = diff

    if max_diff > 0:
        ans = [0 for _ in range(11)]
        for i in comb_cnt:
            ans[10 - i] = comb_cnt[i]
        return ans
    else:
        return [-1]


"""
결국 중복조합 문제로, 시간복잡도를 계산하기 위해선 중복조합의 공식을 알고 있어야 한다.
참고 블로그 : https://kenadams.tistory.com/65

nHr = (r+n-1)! / r!(n-1)! => 20!/10!*10! = 184,775 계산이 가능해진다.

정답률이 20%라는데, 이 문제까지 풀어야 1차는 합격하는 것 같다.
앞에 있던 문제들에 비해 난이도가 높은 편이지만, 완전히 못 풀 정도는 아닌 것 같다.
"""