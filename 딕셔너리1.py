me = {'이름':'hong', 'age':100, 'height':180.5}
you = {'이름':'kim', 'age':90, 'height':170.5}

# 딕셔너리(사전) => {키 : 값,키 : 값}
print(me['이름'])
print(me['age'])
me['age'] = 101
print(me)
print(you)


he = dict()
he['이름'] = 'song'
he['age'] = 200
he['height'] = 130.4
he['weight'] = 100.5
print(he)

del he['height']
print(he)
print(len(he))

print(he.keys())   #key 목록만 가져온 것

for x in he:
    # print(x) #key만 프린트
    print(x,he[x])
