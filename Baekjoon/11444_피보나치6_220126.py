"""
아래 식은 행렬이다.

( F_n+2 ) = ( 1 1 ) ( F_n+1 )
( F_n+1 ) = ( 1 0 ) ( F_n   )
참고 블로그 : https://ataraxiady.github.io/dev/2021/04/15/dev-boj-2_11444/
"""
import sys
# input = sys.stdin.readline
c = 1000000007

# 제곱 구하는 분할 정복
def power(matrix, p):
    if p == 1:
        return matrix
    else: # 2 이상일 때
        temp = power(matrix, p // 2)

        if p % 2 == 0:
            return multi(temp,temp)
        else:
            return multi(multi(temp,temp), matrix)

def multi(matrix1, matrix2): #
    temp = [[0] * 2 for _ in range(2)]

    for i in range(len(matrix1[0])): # 이거 꼭 기억해둬라 2가 아니라, 경우의 수 때문에 len으로 한다.
        for j in range(len(matrix2[0])):
            summary = 0
            for k in range(2):
                summary += matrix1[i][k] * matrix2[k][j]
            temp[i][j] = summary % c
    return temp

# 초기 행렬
mat=[[1,1],[1,0]]
#피보나치 초기값
start=[[1],[1]]

N=int(input())

if N<3:
    print(1)
else:
    print(multi(power(mat,N-2),start)[0][0])