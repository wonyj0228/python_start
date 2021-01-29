member = ['a110', 'b230','c340','a220']

#부서가 a:기획부, b:개발부, c:인사부
#직급이 1:사장, 2:팀장, 3:사원

#1. for문으로 사원번호 3번 추츨
#2. 추출된 사원번호에서 부서,직급값 추츨
#3. 부서, 직급값 판별

for i in range(len(member)):
    code = member[i]  #사원번호 추출3번

    part = code[0]  #부서
    position = code[1]  #직급
    result = ''

    if part == 'a':
        result = '기획부'
    elif part == 'b':
        result = '개발부'
    elif part == 'c':
        result = '인사부'
    else:
        result = '해당 부서가 존재하지 않습니다.'

    if position == '1':
        result = result + ' ' + '사장'
    elif position == '2':
        result = result + ' ' + '팀장'
    elif position == '3':
        result = result + ' ' + '사원'
    else:
        result = '해당 직급이 존재하지 않습니다.'

    print( code,'당신은', result)




