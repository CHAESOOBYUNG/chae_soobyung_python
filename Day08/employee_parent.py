class Employee:
    def __init__(self, name, emptype):
        self.name = name
        self.emptype = emptype

    def print_profile(self):
        print("이름: ", self.name)
        print("고용형태: ", self.emptype)