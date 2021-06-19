# 예제2: 생성자 호출 실험
# 인스턴스 변수는 언제 생성되고 초기화되는가?
# 생성자에서 생성된 인스턴스 변수와 메서드에서 생성된 인스턴스 변수 이름이 동일하다면 어떻게 될까?

class Class1:
    def __init__(self, num):
        self.num = num
        print('## Class1.__init__()')
        print('self.num:', self.num)
        print('id(self): ', id(self))

class Class2:
    def __init__(self, num):
        print('## Class2.__init__()')
        self.obj = Class1(num)
        print('id(self.obj):', id(self.obj))

    def setObj(self, o):
        print('## Class2.setObj()')
        self.obj = o
        print('id(o):', id(o), 'id(self.obj):', id(self.obj))


obj1 = Class2(100)
print()
obj1.setObj(Class1(5000))