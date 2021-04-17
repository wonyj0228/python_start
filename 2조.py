from bs4 import BeautifulSoup
from urllib import request

movie_list = ['136715','145371','129731','141478','145835']
print('====================================')

for index in range (len(movie_list)):
    # 영화제목 , 별평점 , 예매순위 , 누적관객
    con = request.urlopen('https://movie.daum.net/moviedb/main?movieId=' + movie_list[index])
    # print('연결 성공', con)

    doc = BeautifulSoup(con, 'html.parser')

    # 영화이름
    txt_name = doc.select('span.txt_name')
    name = txt_name[0].text
    print('영화이름 : ', name)

    # 평점
    info = doc.select('div.info_origin a.link_grade')
    g = info[0].text
    g_only = g[3:]
    s_g_only = g_only.strip()
    print('   평점 : ' ,s_g_only)

    # 예매순위
    a_rank = doc.select('a.link_txt')
    rank = a_rank[0].text
    r_only =rank[:-1]
    print('예매순위 : ',r_only,'위')

    # 누적관객
    total_a = doc.select('dd a.link_num')
    num = total_a[0].text
    print('누적관객 : ', num)

    print('====================================')

    file_name_list = ['소울(2020)','극장판 귀멸의 칼날','북스마트(2019)','세자매(2020)','명탐정 코난']
    file = open(file_name_list[index] + '.txt', 'w')
    file.write('영화이름 : ' + name + '\n')
    file.write('평점 : ' + s_g_only+ '\n')
    file.write('예매순위 : ' + r_only + '위' + '\n')
    file.write('누적관객 : ' + num + '\n')
    file.close()


