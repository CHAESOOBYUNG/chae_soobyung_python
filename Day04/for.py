list_ive = ["원영", "유진", "리즈", "레이", "이서", "가을"]
for name in list_ive:
    print(name)
print("프로그램 종료")
print()

list_num = [1,2,"3"]
for num in list_num:
    print(num)
print()

list_tuple = [(1,2), (3,4)]
for x, y in list_tuple:
    print(x, y)
print()

# 1부터 100까지 출력
for i in range(1, 11):
    print(i)
print()

# print 함수 특성
print("가", "나", "다", 1, sep="")
print(1, end=" ")
print(2, end=" ")
print(3, end=" ")
print(4)
print()

print(type(range(1, 101)))
num_list = list(range(1, 101))
print(sum(num_list))

count = int(input("몇번 반복하시겠습니까>"))
for x in range(1, count + 1):
    print("실행")

# 최고점과 최저점을 제외하고 평균을 구하세요
score = [10, 9, 8, 9, 7, 4, 6]
score.sort()
del score[0] # 최저점
del score[-1] # 최고점
sum_result = 0
for x in score :
    sum_result += x
print(score)
print("평균", sum_result / len(score))

# 최고값 함수
print(max(score))

# 최저값 함수
print(min(score))

# 반복문, 조건문 조합
for x in range(1, 51):
    if x % 2 ==0:
        print(x, end=" ")
print()

# 1~100의 수 중 7의 배수의 개수
count = 0
for x in range(1, 101):
    if x % 7 == 0:
        count += 1
print("7의 배수의 개수: ", count)
print()

# break문
for x in range(1, 11):
    # continue
    # break
    if x == 4:
        # continue
        break
    print(x)
print()

# for문으로 list 만들기
list_x = []
for x in range(1, 11):
    if x % 2 == 0:
        list_x.append(x)
print(list_x)

list_x = [x for x in range(1, 11) if x % 2 == 0]
print(list_x)
print()

list_A = [1,2,3,4]
list_B = [3,4,5,6]
list_C = []

for x in list_A:
    for y in list_B:
        if x == y:
            list_C.append(x)
print(list_C)