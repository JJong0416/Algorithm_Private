# 문제 이해가 안되서 문제 참고 https://tmdrl5779.tistory.com/119

def binary():
    left, right = 1, max(data)

    while left <= right:
        mid = (left + right) // 2

        count = 1 # 처음거 체크
        wifi = min(data) + mid

        for i in range(1,len(data)):
            if wifi <= data[i]:
                count += 1
                wifi = data[i] + mid

        if count >= C:
            left = mid + 1
        if count < C :
            right = mid - 1

    return right

N,C = map(int,input().split())

data = [int(input()) for _ in range(N)]
data.sort()

print(binary())