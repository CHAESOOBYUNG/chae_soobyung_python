# 회계관리 프로그램 (함수 사용)
# 기능 
# 1) 고객사의 정보를 받아서 회사의 정보를 출력해주는 기능
#    고객사 정보(회사이름, 영업일수, 하루 수익)
# 2) 월 수익을 계산해서 돌려주거나 출력하는 기능
# 3) 계산된 월 수익에 보너스를 추가해서 돌려주는 기능

# # 기능 1
# def print_profile(name, day, dailyMoney):
#     print(f"고객사의 회사명은 {name}이고 영업일수는 {day}이며 하루 수익은 {dailyMoney}입니다.")

# # 기능 2
# def cal_money(day, dailyMoney):
#     return day * dailyMoney

# # 기능 3
# def add_bonus(bonus) :
#     global monthMoney
#     monthMoney += bonus

# def add_bonus_01(bonus) :
#     global monthMoney_01
#     monthMoney_01 += bonus

# name = "메가"
# day = 21
# dailyMoney = 200
# print_profile(name, day, dailyMoney) 
# monthMoney = cal_money(day, dailyMoney)
# print("월수익 : ", monthMoney)
# add_bonus(3333)
# print("보너스 추가된 월수익 : ", monthMoney)


# name_01 = "이투스"
# day_01 = 23
# dailyMoney_01 = 100
# print_profile(name_01, day_01, dailyMoney_01) 
# monthMoney_01 = cal_money(day_01, dailyMoney_01)
# print("월수익 : ", monthMoney_01)
# add_bonus_01(1111)
# print("보너스 추가된 월수익 : ", monthMoney_01)

# 회계관리 프로그램 (클래스 사용)
# 기능 
# 1) 고객사의 정보를 받아서 회사의 정보를 출력해주는 기능
#    고객사 정보(회사이름, 영업일수, 하루 수익)
# 2) 월 수익을 계산해서 돌려주거나 출력하는 기능
# 3) 계산된 월 수익에 보너스를 추가해서 돌려주는 기능

# 데이터, 함수 -> 메소드

# 클래스 선언
class Account :
    # 데이터 세팅 기능
    def set_data(self, name, day, dailyMoney) : # self는 주소값
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

# 객체 생성
a1 = Account()
a2 = Account()
print(id(a1))
print(id(a2))

b1 = 1
b2 = 1
print(id(b1))
print(id(b2))

c1 = [1,2,3]
c2 = [1,2,3]
print(id(c1))
print(id(c2))

# 객체 생성 후 메소드 호출
name = "메가"
day = 21
dailyMoney = 200

a1.set_data(name, day, dailyMoney)
print(a1.name)
print(a1.day)
print(a1.dailyMoney)
a1.sample()
a1.print_profile()
print("월수익 계산 전 : ", a1.result)
a1.cal_money()
print("월수익 계산 후 : ", a1.result)
a1.add_bonus(3333)
print("보너스 추가 후 : ", a1.result)

a2.set_data("이투스", 23, 100)
a2.print_profile()
print("월수익 계산 전 : ", a2.result)
a2.cal_money()
print("월수익 계산 후 : ", a2.result)
a2.add_bonus(1111)
print("보너스 추가 후 : ", a2.result)

