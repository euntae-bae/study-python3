# 예제5: 참조 카운트
class MyClass:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        print(name + ".__init__()")
    def __del__(self):
        print(self.name + '.__del__()')
    def printInfo(self):
        print(self.name + '.value:', self.value)


obj1 = MyClass('obj1', 100)
obj2 = MyClass('obj2', 200)
obj2cp = obj2   # 객체가 복사되는 것이 아니라 참조가 복사된다. 즉, obj2와 obj2cp는 같은 객체를 가리킨다.
print()

obj1.printInfo()    # obj1.value: 100
obj2.printInfo()    # obj2.value: 200
obj2cp.printInfo()  # obj2.value: 200
print()

obj2.value = 10000
obj2.printInfo()    # obj2.value: 10000
obj2cp.printInfo()  # obj2.value: 10000
print()

del obj1    # obj1의 소멸자가 호출된다.
del obj2    # obj2의 참조 카운트가 1 감소한다.
print()
print("end of program")
# end of program이 호출된 후 프로그램이 종료할 때 obj2cp의 소멸자 호출