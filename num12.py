# 다음 문제는 어떻게 풀어야 할까요?
# 같은 값을 가지는 요소는 몇 개 이며, 해당 index와 값은 무엇인가?
C1 = [22, 99, 11, 23]
C2 = [44, 99, 66, 23]

count = 0
number = []
answer = []
for i in range(len(C1)):
    if C1[i] == C2[i]:
        count = count+1
        number.append(i)
        answer.append(C1[i])

print('인덱스의 개수는', count)
print('인덱스의 값은', answer)
print('인덱스 번호는', number )
