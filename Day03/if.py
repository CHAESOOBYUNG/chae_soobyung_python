# 10이상의 값을 입력했을 때만 수행되는 코드
number = int(input("정수를 입력하세요> "))
if number > 10 :
        print("True 수행문")

# 몸무게 입력
weight = int(input("몸무게를 입력하세요> "))
if weight > 80:
        print("다이어트 하세요.")
if weight <= 80:
        print("야식 가능 합니다.")
if weight > 70 and weight <=80:
        print("적절합니다.")
if weight != 65:
        print("65kg이 아닙니다.")

# 숫자 크기 비교
number = float(input("숫자를 입력하세요> "))
if number > 1 :
        print("1보다 큽니다.")
else:
        print("1이하 입니다.")

# 택시 1
money = int(input("보유중인 현금> "))
init_money = 30000
if money > init_money :
        print("택시")
else : 
        print("걸어간다")

# 택시 2
money = int(input("보유중인 현금> "))
init_money = 30000
if money > init_money :
        print("택시")
        talk = input("기사님과 대화? (yes or no)")
        if talk.lower() == "yes":
                print("대화")
        else :
                print("노래를 듣는다")
else : 
        print("걸어간다")  

# 택시 3
money = int(input("보유중인 현금> "))
init_money = 30000

talk = input("기사님과 대화? (yes or no)")

if money > init_money and talk.lower() == "yes":
        print("택시")
        print("대화")
else : 
        print("걸어간다")   

# and, or, not
a = True
b = True
c = False
print(a and b)
print(a and c)
print(a or b)
print(a or c)
print(not c)

# list안 개체 찾기
if 4 in [1, 2, 3, 4]:
        print("4가 있습니다.")
else: 
        print("없습니다.")

