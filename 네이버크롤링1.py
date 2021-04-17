# import bs4      import 만 쓰면 bs4.라는 주소를 추가해야함
# bs4.BeautifulSoup() #beautifulsoup = 클래쓰
from bs4 import BeautifulSoup   #bs4에서 beautifulsoup을 사용할 것이다.

from bs4 import BeautifulSoup
from urllib import request
#urllib은 기본으로 깔려있음 파이썬에
#.을 찍고 프로그램에 깔려있는 기능을 사용할 것이라고 명령하면 됨

con = request.urlopen('http://www.naver.com')  #연결부품획득
print('연결 성공!', con )

doc = BeautifulSoup( con, 'html.parser')   #html을 분석해라
# print('2. 받은 것을 프린트 >> ', doc)
#doc안에는 naver.com의 첫 페이지인 index.html파일의 소스가 통째로 들어있음.

a_nav = doc.select('a.nav') #검색의 결과를 리스트!!
print(a_nav)
print(len(a_nav))
print(a_nav[0])
print(a_nav[0].text)

print(a_nav[7].text)
print(a_nav[8].text)
print(a_nav[9].text)
#슬라이스 x . 리스트안에 있는것을 슬라이스하는건 되지만 text로 한번에 처리는 x
