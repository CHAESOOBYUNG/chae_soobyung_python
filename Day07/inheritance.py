class calParent :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.result = 0

    def add(self):
        self.result = self.x + self.y


cp1 = calParent(1,2)
cp1.add()
print(cp1.result)

# inheritance
class calChild(calParent) :
    def sub(self):
        self.result = self.x - self.y

    def div(self):
        self.result = self.x / self.y

# override
class calChild_02(calChild):
    def div(self):
        if self.y == 0:
            print("0으로 나눌수 없습니다.")
        else:
            self.result = self.x / self.y

# super()
class calChild_03(calChild):
    def div(self):
        if self.y == 0:
            print("0으로 나눌수 없습니다.")
        else:
            super().div()

ch1 = calChild(1,2)
ch1.add()
print(ch1.result)

ch02 = calChild_02(10,0)
ch02.div()
print(ch02.result)

ch03 = calChild_03(10,1)
ch03.div()
print(ch03.result)