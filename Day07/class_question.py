# 클래스 연습 01
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x):
       self.result += x

    def sub(self):
        self.result = self.x - self.y

c1 = Calculator()
c1.add(10)
c1.add(20)
c1.add(30)

c2 = Calculator()
c2.add(1)
c2.add(2)
c2.add(3)

c1.add(30)
print("c1의 계산값 진행중 - ", c1.result)
print("c2의 계산값 진행중 - ", c2.result)

# 클래스 연습 02
class Calculator02:
    def __init__(self, startNum, endNum):
        self.startNum = startNum
        self.endNum = endNum
        self.result = 0
    def sum(self):
        num = startNum
        while(num <= endNum):
            self.result += num
            num += 1
startNum = int(input("startNum : "))
endNum = int(input("endNum : "))
c3 = Calculator02(startNum, endNum)
c3.sum()
print("결과값 : ",c3.result)

# 클래스 연습 03
class Ractangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.result = 0

    def area(self):
        self.result = self.width * self.height

    def circum(self):
        self.result = (self.width + self.height) * 2

width = 3
height = 4
r1 = Ractangle(width, height)
print("사각형의 넓이와 둘레를 계산하라.")
print("가로 : ", r1.width)
print("세로 : ", r1.height)
print("=======================")
r1.area()
print("넓이 : ", r1.result)
r1.circum()
print("둘레 : ", r1.result)