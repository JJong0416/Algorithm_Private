"""
참고 블로그 : https://mizykk.tistory.com/112

1. table에 알파벳 이동 별 거리 체크해두기.
2.
    case1. 알파벳을 딕셔너리에서 찾고 오른쪽으로 이동하기. (오른쪽 이동이므로 + 1된다)
    case2. 중간에 A만 있는 경우에 뒤로 돌아가야한다.
        (ex. BBBAAAAABC 처럼 A가 뭉탱이로 있으면 첫번째 자리로 돌아가 마지막으로 이동하는게 유리하다.)
        a_length = 뭉탱이 A의 길이
        a_index = 뭉탱이 A의 위치
        A 뭉탱이를 만나기 전까지 알파벳 이동수 + 오른쪽 왼쪽 왕복할 이동수 ( ex. 'BBBAABC'에서 'BBB')
        마지막자리로 이동한 후 A 뭉탱이를 만나기전까지 알파벳 이동수 + 왼쪽으로 전진

3. 마지막에는 두 answer중 최소 값을 return

"""
def solution(name):
    table = {}

    for i in range(65, 79):
        table[chr(i)] = i - 65

    for i in range(90, 78, -1):
        table[chr(i)] = 91 - i

    # 3-1. 알파벳 이동수 딕셔너리에서 찾고 오른쪽으로 이동하는 케이스
    right_answer = table[name[0]]  # 첫 글자는 오른쪽으로 이동할 필요가 x
    for i in range(1, len(name)):
        right_answer += table[name[i]] + 1

    # 3-2. 중간에 A만 있는 경우 뒤로 돌아기
    a_length = 0  # A만 있는거의 길이
    for i in range(1, len(name)):
        if 'A' * i in name:
            a_length = i
    a_index = name.find(a_length * 'A')  # 뭉탱이 A 찾기

    left_answer = table[name[0]]
    # A 뭉탱이 전까지는 알파벳 이동수 찾고 오른쪽으로 이동
    for i in range(1, a_index):
        left_answer += table[name[i]] + 2  # 전진한 이후에 첫번째 자리로 가기위해 간 만큼 후진해야하므로 +1이 아닌 + 2

    for i in range(-1, -(len(name) - (a_index + a_length) + 1), -1):
        left_answer += table[name[i]] + 1

    return min(right_answer, left_answer)
