expression = list(map(str, input()))

lst = []  # 빈 리스트 생성
st = []  # 스택 생성
priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  # 우선순위 설정

for i in range(len(expression)):  # 토큰의 길이만큼 반복하여

    if expression[i].isalpha():  # 만약 숫자이면 바로 lst에 추가
        lst.append(expression[i])

    elif expression[i] == '(':  # (이면 바로 stack에 추가
        st.append(expression[i])

    elif expression[i] == ')':  # )가 나오면 stack에서 (가 나올때까지 pop처리 및 lst에 추가.
        while st[-1] != '(':
            lst.append(st.pop())
        st.pop()  # (가 나타나면 pop처리

    else:  # 그외에 경우 tokens[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 tokens[n]의 우선순위가 더 커질때까지 pop
        while st and priority[expression[i]] <= priority[st[-1]]: # 지금 들어온 operand가 st[-1] 값보다 작으면 옮긴다는 뜻
            lst.append(st.pop())  # pop한것들은 lst에 추가 시켜줌
        st.append(expression[i])  # 위의 조건이 완료 되면 stack에 추가

    print(lst, st)

while len(st) != 0:  # stack에 남아있는 연산자들 lst에 추가
    lst.append(st.pop())

print(''.join(lst))

"""
1.  먼저 연산자의 우선순위를 지정한다
2.  *,/가 +,- 보다 우선순위가 높다.
3.  코드를 짤 때는 아래와 같이 미리 우선순위를 설정해놓는것이 편하다.
       priority = {'*':3,'/':3,'+':2,'-':2,'(':1}
4.  하위 표현식으로 만들어질 빈 리스트를 생성
5.  중위표현식을 왼쪽부터 순서대로 읽는다
6.  피연산자이면 2번에서 만들어 놓은 빈 리스트(lst)에 추가한다.
7.  '('이면 stack에 추가하고, ')'이면 stack에서 '('가 나올때까지 스택을 pop()처리 해준 이후 pop()처리 한것들을 2번에서 생성해놓은 list에 추가한다.
8.  선택된게 연산자이면 stack의 위에서 선택된 연산자보다 같거나 높은 우선순위의 연산자들을 pop과 동시에 lst에 추가 해준다. 더 이상 자기보다 같거나 높은 우선순위를 가진 연산자가 없으면 stack에 추가 해준다.
9.  만약 선택된 연산자가 stack 젤 위에 있는 연산자 보다 우선순위가 높다면 다른 처리 없이 바로 stack에 추가해준다.
10. stack에 남아있는 연산자 모두 pop을 하여 lst에 추가 시켜준다.
"""