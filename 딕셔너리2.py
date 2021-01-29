# 내가 좋아하는 장소, 내가 싫어하는 장소, 내가 가보고 싶은 장소 만들기
# 좋아하는 장소가 어떤 것인지 찾아서 프린트
# 가보고 싶은 장소를 '신촌'으로 변경
# 전체 딕셔너리 키/값을 프린트

# 1번
site = dict()
site['좋아하는 장소'] = '바다'
site['싫어하는 장소'] = '산'
site['가보고 싶은 장소'] = '해외'
print(site)
print('좋아하는 장소 : ',site['좋아하는 장소'])
site['가보고 싶은 장소'] = '신촌'
print(site)

# 사전을 만들어보세요. 단어는 5개 이상
# 사전에서 단어를 찾아보세요.
# 사전에 들어있는 전체목록을 프린트

# # 2번
word = dict()
word['사과'] = 'apple'
word['포도'] = 'grape'
word['과일'] = 'fruit'
word['수박'] = 'watermelon'
word['복숭아'] = 'peach'
while True:
    find_word = input('과일이름을 치세요 : ')
    if find_word in word:
        print(word[find_word])
    else :
        print('입력되지않은 단어입니다.')
        break
print(word)

# 전체학기 성적 = {'1학기':100,'2학기':50,'3학기':88,'4학기':99}
# 2학기의 성적은?
# 전체 성적 중 85점이 넘는 학기의 점수 프린트

#3번
grade = {'1학기':100,'2학기':50,'3학기':88,'4학기':99}

print('2학기의 성적은?', grade['2학기'] )

print('------------')

for x in grade:
    if grade[x] > 85:
        print(x,grade[x])
