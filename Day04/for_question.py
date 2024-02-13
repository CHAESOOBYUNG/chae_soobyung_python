# 예제 1
list_num = ['one', 'two', 'three']
for num in list_num:
    print(num)

# 예제 2
sum_result = 0
for i in range(1, 101):
    sum_result += i
print(sum_result)

# 예제 3(구구단)
dan = int(input("단수를 입력하세요: "))
for i in range(1, 10):
    print(f"{dan} X {i} = {dan * i}")
print()

# 예제 4
sum_i = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 2 != 0:
        print(i, end=" ")
        sum_i += i
print()
print("누적합:", sum_i)

# 예제 5
list_score = [90, 25, 67, 45, 80]   
num = 0
for score in list_score:
    num += 1
    if score >= 60:
            print(f"{num}번: 학생은 {score}점으로 합격입니다.")
    else : 
            print(f"{num}번: 학생은 {score}점으로 불합격입니다.")

# 예제 6
number = int(input("정수를 입력하세요: "))
for i in range(1, number + 1):
     if number % i == 0:
        print(i, end=" ")
print()

# 예제 7
list_blood_type = ['b', 'b', 'ab', 'a', 'b', 'a', 'b']

for blood in list_blood_type:
    if blood == "a":
        print("당첨입니다.")
        break
    else:
        print("낙첨입니다.")
print()

# 예제 8
list_result = []
for i in range(1, 101):
    if i % 3 == 0:
        list_result.append(i)
print(list_result)

# 예제 9
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}", end=" ")
    print()

