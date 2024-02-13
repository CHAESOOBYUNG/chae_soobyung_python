# 함수
# 연습문제 01
def mul(x, y):
    return x * y
print(mul(3,4))

# 연습문제 02
def square(a):
    return a ** 2
print(square(5))

# 연습문제 03
# 홀짝 판별 함수
def isEven(a):
    if a % 2 == 0:
        return True
    else:
        return False
print(isEven(9))

# 연습문제 04
import math
def circle_area(r):
    circle_square = (r ** 2) * math.pi
    return circle_square
r = float(input("반지름의 길이를 입력하세요> "))
print (f"원의 넓이: {circle_area(r)}")

# 입력값은 있지만 결과값이 없는 함수 
# 연습문제 01
def hello(name):
    print(name, 'hello')
print(hello("메가스터디"))

# 연습문제 02
def minus(x, y):
    print(x-y)

minus(10, 3)

# 연습문제 03
def divmod_mine(x, y):
    return (x/y, x%y)
print(divmod_mine(10,3))

# 연습문제 04
def english_word(word):
    return word.lower().count('a')

word = input('영어 단어를 입력하세요: ')

print("'a'의 개수: ", english_word(word))

# 연습문제 05
def func_up(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)

sample = [5, 1, 3, 7, 2, 9]
func_up(sample)

# 입력 값이 여러개인 함수
# 예제 01
def num_plus(*args):
    result = 0
    for i in args:
        result += i
    return result
result = num_plus(1,2,3,4,5)
print(result)

# 예제 02
def get_average_many(*args):
    sum = 0
    for i in args:
        sum += i
    avg = sum / len(args)
    return avg
result = get_average_many(1, 32, 51, 32, 20, 50, 60, 60)
print("평균: ", result)

# 예제 03
def names_func(name, *names):
    print(name)
    print(names)
names_func('서울시', '강남구', '메가스터디', '4층', 'python')

# 선택적 함수
# 연습문제
def calc(num1, num2):
    num3 = 0
    if q == "+":
        num3 = num1 + num2
        return num3
    if q == "-":
        num3 = num1 - num2
        return num3
    if q == "*":
        num3 = num1 * num2
        return num3
    if q == "/":
        num3 = num1 / num2
        return num3
        
q = input("어떤 연산을 하실건가요? (+,-,*,/)")
num1 = float(input("첫번째 정수를 입력하세요."))
num2 = float(input("두번째 정수를 입력하세요."))
result = calc(num1, num2)
print(f"{num1}과 {num2}의 {q}연산 결과는 {result}입니다.")

# 함수연습 4


# 함수연습 5
def starCount(layer) :
    # layer라는 매개변수의 값을 가공하여 별을 찍어내고 그 개수의 합을 
    # 출력해주는 기능
    sum_result = 0
    for count in range(layer+1):
        print("*"*count)
        sum_result += count
    print("총 별의 개수 : ", sum_result) 

starCount(6)

# 함수연습 6