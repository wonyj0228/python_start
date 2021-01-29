food = ['아이스크림','아이스아메리카노','생수'] #목록(list - 여러개를 묶을 땐 대괄호)
# 목록을 알고있는 경우와 모르고 있는 경우 방법이 다름
# hobby = []
print(food[0])
print(food[1])
print(food[2])
#data는 0부터 저장이 되기 때문에 3가지의 data가 있을 경우 0, 1, 2 를 활용하여 출력할 수 있다.


for i in range(0,3) :
    print(food[i], end=' ')
#변수 i의 범위를 설정해 0번째 리스트부터 3개까지 리스트로 묶여있는 것을 나열.
# 오리지날 for 문

print() #한줄띄기

for x in food:  #for-each
    print(x, end=' ')
#food리스트에 있는 데이터를 각각 출력하는 것을 전부 반복

print()
print('목록의 개수는 ', len(food))  #len은 개수를 세는 함수



########
# 오늘 끝나고 나서, 할 일 5가지를 목록으로 만들어 보세요.
# 2가지 방식으로 프린트!

to_do = ['저녁먹기','복습하기','씻기','잠자기','영화보기']

for i in range(0,len(to_do)) :
    print(to_do[i],end=' ')
#변수 i에 to_do 리스트의 개수만큼 0부터 숫자를 지정하고 출력하는 것을 반복
print()

for x in to_do :
    print(x,end=' ')
#to_do 리스트 자체를 변수 x로 지정해 x를 전부 출력
print()
print('할 일의 개수는', len(to_do),'개!!!')
#to_do 리스트 안에 있는 데이타를 세는 함수를 활용