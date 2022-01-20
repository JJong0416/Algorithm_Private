import sys
input = sys.stdin.readline

N = int(input())
colors = [list(map(int,input().split())) for _ in range(N)]
min_val = int(1e9)


for i in range(1,N): # 집 하나당
    colors[i][0]= colors[i][0] + min(colors[i-1][1],colors[i-1][2]) # 현재 색 칠하기 + 이전 집의 다른 색들
    colors[i][1]= colors[i][1] + min(colors[i-1][0],colors[i-1][2])
    colors[i][2]= colors[i][2] + min(colors[i-1][0],colors[i-1][1])

print(min(colors[N-1]))
