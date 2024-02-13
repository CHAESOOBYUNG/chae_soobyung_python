import employee_parent

class Permanent(employee_parent.Employee):
    def __init__(self, name, emptype, money, bonus):
        super().__init__(name, emptype)
        self.money = money
        self.bonus = bonus
        self.pay = self.money + self.bonus
    
    def print_profile(self):
        super().print_profile()
        print("급여: ", self.pay)
    
class Temporary(employee_parent.Employee):
    def __init__(self, name, emptype, time, t_money):
        super().__init__(name, emptype)
        self.time = time
        self.t_money = t_money
        self.pay = self.time * self.t_money

    def print_profile(self):
        super().print_profile()
        print("급여: ", self.pay)

run = True
while run:
    emptype = input("고용형태 선택(정규직<P>, 비정규직<T>) : ")
    if emptype.lower() == "p":
        name = input("이름 : ")
        emptype = "정규직"
        try:
            money = int(input("기본급: "))
            bonus = int(input("보너스 : "))
        except ValueError:
            print("숫자가 아닌것 같은데요?")
            continue
        print("=====================")
        per_employee = Permanent(name, emptype, money, bonus)
        per_employee.print_profile()
        break
    elif emptype.lower() == "t":
        name = input("이름 : ")
        emptype = "비정규직"
        try:
            time = float(input("작업시간 : "))
            t_money = int(input("시급 : "))
        except ValueError:
            print("숫자가 아닌 것 같은데요?")
            continue
        print("=====================")
        temp_employee = Temporary(name, emptype, time, t_money)
        temp_employee.print_profile()
        break
    else: 
        print("지원하지 않는 고용형태입니다. 입력을 다시하세요!")
          