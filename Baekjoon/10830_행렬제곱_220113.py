# 행렬 곱셈 함수
def matrix_mult(A, B):
    temp = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                temp[i][k] += A[i][j] * B[j][k]
            temp[i][j] %= 1000
    return temp


def matrix_pow(A, n): # 재귀로 문제 풀기
    if n == 1:
        return A
    if n % 2 == 0:
        temp = matrix_pow(A, n//2) #짝수일 때
        return matrix_mult(temp, temp)
    else:
        temp = matrix_pow(A, n-1) # 홀수일 때
        return matrix_mult(temp, A)


N,b = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

ans = matrix_pow(data,b)



for a in range(len(data)):
    for b in range(len(data[0])):
        print(ans[a][b] % 1000, end=' ')
    print()




# 붐버맨 실버2
# from collections import deque
#
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
#
# R,C,N = map(int,input().split())
# data = [list(map(int,input().split())) for _ in range(C)]
#

