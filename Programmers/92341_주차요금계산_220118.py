import math

def calc_time(t1, t2):
    h1, m1 = t1.split(':')
    h2, m2 = t2.split(':')

    tot1 = int(h1) * 60 + int(m1)
    tot2 = int(h2) * 60 + int(m2)

    return abs(tot1 - tot2)


def solution(fees, records):
    price = dict()
    st = dict()
    ans = []
    check = []

    for record in records:
        time, number, order = record.split(' ')

        if order == "IN":
            st[number] = time

            if number not in price.keys():
                price[number] = 0  # 단 한번도 안들어왔다면

        if order == "OUT":
            in_time = st[number]
            price[number] += calc_time(time, in_time)
            del st[number]

    if st:
        final = "23:59"
        for number, time in st.items():
            price[number] += calc_time(final, time)

    for number, t in price.items():
        number, t = int(number), int(t)

        if t < fees[0]:
            ans.append((number, fees[1]))
        else:
            tmp = fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3]
            ans.append((number, tmp))

    ans = sorted(ans, key=lambda x: x[0])

    for i in ans:
        n, t = i
        check.append(t)

    return check

"""
당일날에도 풀고, 이번에 다시 풀어봐도 풀었다. 저번에는 1시간 조금 더 걸렸던 것 같은데
이번엔 1시간 안에 다 푼 것 같아서 기분은 좋지만, 그래도 아직 부족한게 느껴지긴 하다.
dictionary 활용 + 올림 함수에 대해서 한번만 체크하고 넘어가면 될 것 같다
"""