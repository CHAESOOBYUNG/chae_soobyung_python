# 1. 어떤 기능을 하는 함수를 만들지 생각
# 2. 매개변수로 어떠한, 몇개의 값이 필요할지 생각
# 3. 함수를 호출한 곳으로 어떤 값을 돌려줘야 할지(return)
# 4. 구현

# 기본 구조
def 함수명(매개변수) :
    pass

# 숫자 2개를 매개변수로 전달하면 그 합을 돌려주는 함수
# a = 10
# b = 20
# result = a + b 
# print(result)

def sum_num02(a, b):
    return a + b

print(sum_num02(10, 20))

def pow2(a, b):
    result = 1
    for count in range(b):
        result *= a
    return result
print(pow2(4, 3))

a = 2
def sum0(a):
    a += 1
    return a
result = sum0(a)
print(result)
print(a)

# 권장하지 않음
result = 2 # 전역변수
def sum1(a) :
    global result # 전역변수 정의
    result = result + a 
    return result

sum_result = sum1(1)
print(sum_result)

# 권장
result = 2 # 전역변수
def sum2(a) :
    result_sum = result + a
    return result_sum

sum_result = sum2(1)
print(sum_result)

# 입력값은 있지만 결과값은 없는 함수
def hello(name):
    print(name)

hello("채수병")

# 입력값은 없지만 결과 값이 있는(없는) 함수
def warning():
    print("1~2시 서버 업데이트")

warning()

# 입력값이 몇 개인지 모를 때 함수
def plus(*num):
    sum_result = 0
    for x in num:
        sum_result += x
    return sum_result

print(plus(1,2,3,4,5))
print(plus(1,2,3))

# 입력 값이 여러개인 함수
def cal1(choice, *data):
    if choice == "+":
        print(sum(data))
    else:
        print("지원하지 않는 연산입니다.")

cal1("+",1,2,3,4,5)

# 평균, 분산, 표준편차
import statistics
list1 = [1,2,3,4]
print(statistics.mean(list1)) # 평균
print(statistics.variance(list1)) # 분산
print(statistics.stdev(list1)) # 표준편차

def statistics_func(choice, *data) :
    if choice == "평균":
        return statistics.mean(data)
    elif choice == "분산":
        return statistics.variance(data)
    elif choice == "표준편차":
        return statistics.stdev(data)
    else :
        return "에러"

print(statistics_func("평균",1,2,3,4))
print(statistics_func("분산",1,2,3,4))
print(statistics_func("표준편차",1,2,3,4))

# 함수의 return 값이 2개 이상일 경우
def sum3(a, b):
    result1 = a + b
    result2 = a * b
    result3 = a // b
    return result1, result2, result3
result = sum3(1,2)
print(result)

# 기본적으로 덧셈 기능 + 내가 옵션을 주면 다른 기능으로 바뀌는 계산

# def print(msg, end="\n", sep=" ")

def sum4(a, b, choice="+"):
    if choice == "+": 
        return a + b
    elif choice == "-":
        return a - b
    else:
        pass

print(sum4(1,2))
print(sum4(1,2,"-"))