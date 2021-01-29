# import bs4      import 만 쓰면 bs4.라는 주소를 추가해야함
# bs4.BeautifulSoup() #beautifulsoup = 클래쓰
from bs4 import BeautifulSoup   #bs4에서 beautifulsoup을 사용할 것이다.

from bs4 import BeautifulSoup
from urllib import request
#urllib은 기본으로 깔려있음 파이썬에
#.을 찍고 프로그램에 깔려있는 기능을 사용할 것이라고 명령하면 됨

con = request.urlopen('https://finance.naver.com/item/main.nhn?code=005930')  #연결부품획득
print('연결 성공!', con )

name = '삼성전자'

doc = BeautifulSoup( con, 'html.parser')   #html을 분석해라
# print('2. 받은 것을 프린트 >> ', doc)
#doc안에는 naver.com의 첫 페이지인 index.html파일의 소스가 통째로 들어있음.

span_code = doc.select('span.code') #.select = 검색의 결과를 리스트로!!
print('code의 개수 >> ', len(span_code))
code =  span_code[0].text
print('code : ' , code)

div_today = doc.select('div.today')
print(len(div_today))
today1 = div_today[0].select('span.blind')
# today2 = div_today.select('span.blind')
# 개수가 하나라도 리스트에서 자료를 추출해오는 것이기 때문에 [0] 꼭 같이 넣어줘야 함
print(today1)
print(today1[0])
print(today1[0].text)

span_blind = doc.select('span.blind')
print(len(span_blind))

for index in range(len(span_blind)):
    print(index,': ', span_blind[index].text)
#for문을 index 결합해서 span.blind에 들어있는 자료들을 전부 출력 가능
#뭐가 현재가이고 고가인지 자료를 보면서 비교가능. 자료출력했을때 증시가격이랑 다를 수 있음.



#div안에 있는 것 중 span.blind를 찾는 새로운 방법

all = doc.select ('div.today span.blind')
#바로 밑에있는것을 찾을때 'div.today > span.blind
print(len(all))
print(all[0])

# 삼성전자 전일, 고가, 시가, 저가
# yes, high, low, start

print('code : ' , code)
yes = span_blind[15].text
print('전일: ', yes)
high = span_blind[16].text
print('고가: ', high)
low = span_blind[20].text
print('저가: ', low)
start = span_blind[19].text
print('시가 ', start)

file = open(name + '.txt', 'w')
#전체 코딩파일을 txt파일로 저장한다는 뜻
#파일이름+. txt / 파일에 저장할것기 때문에 w
file.write(code + '\n')
file.write(yes + '\n')
file.write(high + '\n')
file.write(low + '\n')
file.write(start + '\n')
file.close()
#파일 닫기까지
