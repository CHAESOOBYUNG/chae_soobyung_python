# 외장함수 사용법
import random
# from random import randint
# print(randint(1, 10))

while True:
    list_size = int(input("리스트의 크기를 정하세요! "))
    if list_size <= 10:
        break
    else:
        print("리스트의 크기를 10 이하로 다시 할당하세요!")

num = 0 
list1 = []
while num < list_size:
    num += 1
    item = random.randint(1, 100)
    list1.append(item)
print(list1)

# final test01
num_random = random.randint(1, 10) # 1 ~ 10 사이의 난수 발생
while True:
    var = int(input("1~10사이의 정수를 입력하세요: "))
    if num_random == var:
        print("성공")
        break
    elif num_random > var:
        print("더 큰 값을 입력하세요")
    else: 
        print("더 작은 값을 입력하세요")

# final test02
msg = '''비 갠 뒤에 비애 대신 a happy end 
비스듬히 씩 비웃듯 칠색 무늬의 무지개
철없이 철 지나 철들지 못해 (still)'''
words = []  # 단어들을 저장할 빈 리스트를 생성합니다.
word = ""   # 현재 단어를 저장할 변수를 초기화합니다.
index = 0   # 문자열을 순회하기 위한 인덱스 변수를 초기화합니다.

# 문자열의 끝까지 반복합니다.
while index < len(msg):
    # 현재 문자가 공백이 아니라면 단어에 추가합니다.
    if msg[index] != ' ' and msg[index] != '\n':
        word += msg[index]
    # 현재 문자가 공백이거나 줄바꿈 문자라면 단어가 완성된 것이므로 리스트에 추가하고 단어를 초기화합니다.
    else:
        if word:  # 빈 문자열이 아닌 경우에만 단어를 리스트에 추가합니다.
            words.append(word)
            word = ""
    index += 1

# 마지막 단어를 처리합니다.
if word:
    words.append(word)

print("단어 리스트:", words)
print("단어 개수: ", len(words))

# 별첨 알고리즘(최대/최소값)
num_random2 = random.randint(1, 100) # 1~100사이의 난수 발생    
list2 = []
for x in range(1, 11) :
    list2.append(random.randint(1, 100))

max_num = min_num = list2[0]
for x in list2:
    if max_num < x:
        max_num = x
    if min_num > x:
        min_num = x

print(list2)
print("최대값: ", max_num)
print("최소값: ", min_num)
    
# 별첨 알고리즘(선택 정렬)
a = [5, 1, 3, 7, 2, 9]
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a)