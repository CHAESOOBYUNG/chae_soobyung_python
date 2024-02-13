# 예제 1
pushup = 0
while pushup < 10:
    pushup += 1
    print(f"푸쉬업 {pushup}회 수행했습니다.")
print("오늘 운동을 끝마칩니다.")

# 예제 2
# for 문
sum1 = 0
for i in range(1, 101):
    sum1 += i
print(sum1)
# while 문
num = 0
sum2 = 0
while num < 100:
    num += 1
    sum2 += num
print(sum2)

# 예제 3
msg = '''
1. Add
2. Del
3. List
4. Quit'''

# num = 9999
# while num != 4:
#     print(msg)
#     num = int(input("Enter Number : "))
#     if num == 4:
#         print("종료되었습니다.")
    
while True:
    print(msg)
    num = int(input("Enter Number : "))
    if num == 4:
        print("종료되었습니다.")
        break

# 예제 4
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
    item = int(input("리스트에 값을 할당해보세요! "))
    list1.append(item)
print(list1)

# for 문
list2 = []
for num in range(list_size):
    num += 1
    item = int(input("리스트에 값을 할당해보세요! "))
    list2.append(item)
print(list2)

# 예제 5
num = 1
sum = 0
while True:
    sum += num
    if num == 100:
        print(f"1부터 {num}까지의 덧셉 종료")
        break
    num += 1

print(f"결과: {sum}")

# 예제 6
pushup = 0
while True:
    pushup += 1
    if pushup == 11:
        print("오늘 운동을 끝마칩니다.")
        break
    print(f"푸쉬업 {pushup}회 수행했습니다.")

# 예제 7
num = 0
while num < 100:
    num += 1
    if num % 2 == 0:
        continue
    print(num, end=" ")

# 예제 8
pushup = 0
while True:
    pushup += 1
    if pushup == 11:
        print("오늘 운동을 끝마칩니다.")
        break
    if pushup % 7 == 0:
        print("휴식을 취합니다.")
        continue
    print(f"푸쉬업 {pushup}회 수행했습니다.")