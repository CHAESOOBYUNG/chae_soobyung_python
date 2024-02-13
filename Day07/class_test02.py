# 생성자 사용
class Cal :
    def __init__(self, check): # 생성자
        print("실행되었습니다.", check)

c1 = Cal(1) # 생성자(메소드의 한 종류)의 소괄호

class Account :
    # 데이터 세팅 기능
    def __init__(self, name, day, dailyMoney) : # self는 주소값
        self.name = name # self.name은 heap 영역의 name 변수를 의미
        self.day = day
        self.dailyMoney = dailyMoney
        self.result = 0

    # 기능 1
    def print_profile(self):
        print(f"고객사의 회사명은 {self.name}이고 영업일수는 {self.day}이며 하루 수익은 {self.dailyMoney}입니다.")

    # 기능 2
    def cal_money(self):
        self.result = self.day * self.dailyMoney

    def sample(self):
        print("출력합니다.")

    # 기능 3
    def add_bonus(self, bonus) :
        self.result += bonus

a1 = Account("메가", 21, 200)
a1.print_profile()
print("월수익 계산 전 : ", a1.result)
a1.cal_money()
print("월수익 계산 후 : ", a1.result)
a1.add_bonus(3333)
print("보너스 추가 후 : ", a1.result)

class Sample:
    def __init__(self):
        print("self의 의미: ", self)

s1 = Sample()
print("s1 객체의 주소 : ", hex(id(s1)))

s2 = Sample()
print("s2 객체의 주소 : ", hex(id(s2)))

class Sample2 :
    count = 0 # 클래스 변수
    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Sample2.count += 1

s1 = Sample2("이름1") 
print(s1.name)
print("s1 객체로 본 count: ", s1.count)
s2 = Sample2("이름2")
print(s2.name)
print("s1 객체로 본 count: ", s1.count)
