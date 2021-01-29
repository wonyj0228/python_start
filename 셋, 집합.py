#set(집합)
# 중복을 허용하지 않음.

jumsu_list = [100,30,50,60,30,100]
jumsu_set = set(jumsu_list)
print(type(jumsu_set))   #jumsu_set의 타입을 알 수 있게 해줌.
#<class 'set'> = set 타입이라는 뜻.
print(jumsu_set)


jumsu_list2 = [50, 60, 30, 120, 120]
jumsu_set2 = set(jumsu_list2)
print(jumsu_set2)
result = jumsu_set2.intersection(jumsu_set)  #교집합
print(result)