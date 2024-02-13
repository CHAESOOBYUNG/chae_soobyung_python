class Parent :
    def speak(self):
        print("상속 후 오버라이딩하여 사용하세요")
        raise Exception

class Mine(Parent):
    def speak(self) :
        print("오버라이딩하여 사용중입니다.")

m1 = Mine()
m1.speak()