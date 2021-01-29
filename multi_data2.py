hobby = []
hobby.append('코딩')
#hobby라는 리스트에 '코딩'이라는 데이타를 입력
print('개수 >>', len(hobby))
#hobby리스트에 입력된 데이타 수를 함수로 계산해 출력
hobby.append('등산')
#hobby리스트에 '등산'이라는 데이타를 입력 -> 파이썬 특징상 입력된 데이터가 쌓임
print('개수 >>', len(hobby))
#쌓인 데이터수만큼 함수로 계산,출력

for _ in range(3): #3번 반복할 것
    data = input('당신의 새로운 취미는 >>> ') #새로운 취미를 input해 데이터 생성
    hobby.append(data) #입력된 데이터 hobby 리스트에 입력
#따라서, input->append 과정이 3번 반복됨

print('개수 >> ', len(hobby))
#기존에 입력된 '코딩','등산' 데이터에 추가로 input된 3개의 데이터가 리스트에 추가로 입력되었음
#따라서 hobby리스트에 입력된 데이타는 총 5개. len함수가 출력

for x in hobby:
    print(x)
#hobby 리스트에 입력된 데이터들을 x변수에 대입. x변수에 대입된 hobby가 전부 출력.