my_life = '나는 열심히 살자가 인생의 목표예요.!'
#string 도 인덱싱을 가지고 있다.
print(my_life[0])    #'나' 출력
print(my_life[0:2])  #'나는' 슬라이싱 출력

#my_life 를 공백을 기준으로 5개의 string으로 분리 가능
my_life_list = my_life.split(sep=' ')  #string의 리스트 / sep(seperator) = 구분자, 구분을 짓은 기준
#list를 변수로 묶어줌. => RAM으로 옮겨서 원하는 단어만 가져올 수 있게
print(my_life_list)
print(my_life_list[0]) #나는 이 추출됨
print(my_life_list[1])

#1 주민번호
social_no = input('주민번호를 입력하세요. 000000-0000000 >>')   #string임. ''를 넣었으니까
b_year = int(social_no[0:2])
age = 2021 - (1900 + b_year) + 1 #한국나이
print('당신의 나이는', age , '세')

#성별 출력하기
gender = int(social_no[7])
if gender == 1 or gender == 3:
    print('당신의 성별은 남자입니다.')
elif gender == 2 or gender == 4:
    print('당신의 성별은 여자입니다.')
else :
    print('잘못된 입력값입니다.')
