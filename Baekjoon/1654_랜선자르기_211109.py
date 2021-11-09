import sys

K, N = map(int, input().split())
lans = [int(sys.stdin.readline()) for _ in range(K)]
left, right = 1, max(lans)

while left <= right:
    tot = 0
    mid = (left + right) // 2

    for i in lans:
        tot += i // mid

    if tot >= N: 
        left = mid + 1
    else:
        right = mid - 1

print(right)