food_list = ['맛나피자','새로피자','대왕햄버거','군대햄버거']

# 파이썬은 list에서 끝에서부터 가져오는게 가능함


#피자집 개수, 햄버개 개수 프린트

#스크립트
#1. food_list에서 하나씩 추출
#2. 추출값에 피자/햄버거가 있는지 확인 후 추출
#3. 추출된 값의 개수를 프린트

c_pizza = 0
c_hamburger = 0

for food in food_list:
    if '피자' in food:
        c_pizza += 1
    elif '햄버거' in food:
        c_hamburger += 1
    else:
        pass

print('피자가게 개수는 :',c_pizza,'\n햄버거가게 개수는 :',c_hamburger)

############ in 연산자 안쓰고 가져오기############

count_p = 0
count_h = 0

for i in range(len(food_list)):
    last_food = food_list[i]
    if last_food[2:] == '피자':
        count_p += 1
    elif last_food[2:] == '햄버거':
        count_h += 1
    else:
        pass
print('피자가게 개수는 :',c_pizza,'\n햄버거가게 개수는 :',c_hamburger)