# 연습문제 1
money = 13000
if money >= 30000:
        print("택시를 타시오")
else: 
        print("걸어가시오")

# 연습문제 2
money = int(input("현재 얼마가 있나요?"))
if money >= 30000:
        print("택시를 타시오")
else: 
        print("걸어가시오")

# 연습문제 3
a = int(input("정수를 입력하세요>"))
b = int(input("정수를 입력하세요>"))
if a > b:
        print(a)
else:
        print(b)

# 연습문제 4
load = int(input("짐의 무게는 얼마입니까?"))
if load < 10:
        print(f"짐의 무게는 {load}kg이며 수수료는 없습니다.") 
else:
        fee = 10000 * (load // 10)
        print(f"짐의 무게는 {load}kg이며 수수료는 {fee}입니다.")    

# 연습문제 5
money = int(input("현재 얼마가 있나요?"))
if money >= 30000:
        print("택시를 타시오")
        talk = input("기사님과 대화를 하시겠습니까?")
        if talk.lower() == "yes":
                print("대화를 하라")
else:
        print("걸어가시오")

# 연습문제 6
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input("숫자 하나를 입력하세요> "))

if number in num_list :
                print(f"입력하신 숫자는 num_list[{num_list.index(number)}]에 존재합니다.")
else :
        print(f"해당값 {number}은/는 리스트에 포함되지 않았습니다.")

# 연습문제 7
money = 13000
hungry = input("배가 고픈가요?")
if money >= 10000 and hungry.lower() == "yes":
        print("저녁을 사먹으시오")
else:
        print("집에 가시오")

# 연습문제 8
moeny = 8000
hungry = input("배가 고픈가요?")
if money >= 10000 or hungry.lower() == "yes":
        print("저녁을 사먹으시오")  
else: 
        print("집에 가시오")     

# 연습문제 9
number = int(input("정수를 입력하세요> "))
if number % 2 == 0:
        print(f"정수 {number}는 짝수입니다.")
else:
        print(f"정수 {number}는 홀수입니다.")

# 연습문제 10
number = int(input("두자리 정수를 입력하세요> "))
if number % (number / 10 + number % 10) == 0:
        print(f"{number}는 하샤드 수입니다.")
else: 
        print(f"{number}는 하샤드 수가 아닙니다.")