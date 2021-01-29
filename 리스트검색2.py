
#나의 사원번호 = a110= a :부서 / 1 : 직급 / 10 : 나의 번호
#부서가 a:기획부, b:개발부, c:인사부
#직급이 1:사장, 2:팀장, 3:사원

#a110, b230, c340를 구해봐라.

#순차문의 구조 : 입력 ---> 처리 ---> 출력

#입력
#파이썬에서는 들여쓰기(indent라고함. 블럭설정후 tap키하면 들여쓰기됨. shift_tab키는 반대로)
while True :
    code = input('본인의 사원번호를 입력하세요.(종료 = x) : ')
    if code == 'x':
        print('시스템을 종료합니다.')
        break
#처리

#1.입력한 데이터 중에서 부서와 직급을 추출한다.
#2.부서의 값에 따라서 부서를 판별한다.
#3.직급의 값에 따라서 직급을 판별한다.
# 스크립트 써서 처리 순서를 생각해보기!!!

    dep = code[0] #부서
    deg = code[1] #직급
    result = ''   #찍어줄 스트링!을 모아줄 변수

    if dep == 'a':
        result = '기획부'
    elif dep == 'b':
        result = '개발부'
    elif dep == 'c':
        result = '인사부'
    else:
        print('\n해당 부서가 존재하지 않음.')
#\n을 넣으면 앞에 엔터가 들어가게 되는 것 (유라인?이라고 함)

    if deg == '1':
        result = result + ' ' + '사장'
    elif deg == '2':
        result = result + ' ' + '팀장'
    elif deg == '3':
        result = result + ' ' + '사원'
    else:
        print('\n해당 직급이 없음.')

    print('당신은', result)