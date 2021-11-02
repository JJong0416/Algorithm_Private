import sys

input = sys.stdin.readline

text1 = str(input()).strip()
text2 = str(input()).strip()

len_text1 = len(text1)
len_text2 = len(text2)

data = [[0] * (len_text2 + 1) for _ in range(len_text1 + 1)]

for i in range(1, len_text1 + 1):
    for j in range(1, len_text2 + 1):
        if text1[i - 1] == text2[j - 1]:
            data[i][j] = data[i - 1][j - 1] + 1
        else:
            data[i][j] = max(data[i - 1][j], data[i][j - 1])

print(data[-1][-1])
