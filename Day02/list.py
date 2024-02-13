# 리스트 - 길이, 값 수정 가능
list_num = [10, 20, 30, 40, 50]
print(type(list_num), list_num)

list_name = ["김", "이", "박", "최"]
print(list_name)

list_mix = ["일", "이", 3, 4]
print(list_mix)

# 리스트 인덱싱
print(list_num[0])
print(list_num[1])

# 리스트 슬라이싱
print(list_num[0:3])

list_02 = [[1, 2],[3, 4], [5, 6]]
print(list_02[2][0])

# 예제 1
list_ex1 = ['a', 'b', 'c', [1, 2, 3]]
number = list_ex1[3]
print(number)
print(number[0] + number[2])
print(list_ex1[3][0] + list_ex1[3][2])

list_01 = [1, 2]
list_02 = [3, 4]
# 리스트 더하기
print(list_01 + list_02)
# 리스트 곱하기
print(list_01 * 3)

# 문자열 길이 구하기
msg = "python is fun"
print(len(msg))

# 리스트 길이 구하기
list_num = [1,2,3,4,5,6,10,11,14]
print(len(list_num))

# 주소 값(메모리 값) 확인
a = 1
print(id(a))
a = 2
print(id(a))

# 리스트 값 수정 (함수 사용 x)
print("수정전: ", id(list_num), list_num)
list_num[4] = 50
print("수정후1: ", id(list_num), list_num)
list_num[3:] = [40]
print("수정후2: ", id(list_num), list_num)
list_num[3] = [70, 80, 90]
print("수정후3: ", id(list_num), list_num)

# 리스트 값 삭제 (함수 사용 x)
list_num[3:] = []
print("삭제후1: ", id(list_num), list_num)

# 리스트 값 삭제 (del 함수)
del list_num[2]
print("삭제후2: ", id(list_num), list_num)
del list_num[1:2]
print("삭제후3: ", id(list_num), list_num)

# 리스트 값 삭제 (remove 함수) - remove(원하는 값)
list_num = [1, 2, 3, 4, 5]
list_num.remove(2)
print("삭제후4: ", id(list_num), list_num)

# append() - 하나의 데이터를 뒤에 이어 붙이는 함수
list_num = [1, 2, 3, 4, 5]
list_num.append(6)
print("수정후1: ", id(list_num), list_num)
list_num.append([7, 8, 9])
print("수정후2: ", id(list_num), list_num)

# insert() - 하나의 데이터를 원하는 위치에 삽입하는 함수
list_num.insert(2, 25)
print("수정후3: ", id(list_num), list_num)

# extend() - 여러개의 데이터를 뒤에 확장하는 함수
list_num.extend([1, 2, 3, 4, 5, 6])
print("수정후4: ", id(list_num), list_num)

# sort() - 오름차순으로 분류하는 함수
list_name = ["박효신", "이수", "김범수", "나얼"]
list_name.sort()
print(list_name)

# reverse() - 역정렬 함수
list_name.reverse()
print(list_name)

# 예제 2 - 내림차순
list_lang = ['banana', 'cat', 'egg', 'apple', 'door']
list_lang.sort(reverse=True)
# list_lang.sort()
# list_lang.reverse()
print(list_lang)

# count(), index() 함수
list_num = [10, 20, 30, 40, 50, 10, 10]
print(list_num.count(10))
print(list_num.index(30))

# pop() 함수
list_lang = ['banana', 'cat', 'egg', 'apple', 'door']
print(list_lang.pop(2))
print(list_lang)

# split() 함수
msg = "I like python"
print(msg.split(" "))

# join() 함수
msg_list = ['I', 'like', 'python']
print(" ".join(msg_list))