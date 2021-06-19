# 예제1: 인스턴스 변수, 메서드, 생성자
# //: 몫, %: 나머지
# /: 나눗셈
# is: 서로 같은 객체인지, 즉 서로 같은 대상을 가리키는지 확인한다.

class Calc:
    def __init__(self, n1, n2):
        print('## __init__()')
        self.num1 = n1 # 인스턴스 변수 num1
        self.num2 = n2 # 인스턴스 변수 num2
        #print('n1:', id(n1), 'n2:', id(n2))
        #print('num1:', id(self.num1), 'num2:', id(self.num2))
        print('n1 is self.num1', n1 is self.num1)
        print('n2 is self.num2', n2 is self.num2)

    def setData(self, n1, n2):
        print('## setData()')
        self.num1 = n1 # num1의 참조를 n1의 참조로 바꾼다.
        self.num2 = n2 # num2의 참조를 n2의 참조로 바꾼다.
        #print('n1:', id(n1), 'n2:', id(n2))
        #print('num1:', id(self.num1), 'num2:', id(self.num2))
        print('n1 is self.num1', n1 is self.num1)
        print('n2 is self.num2', n2 is self.num2)

    def add(self):
        print('add()')
        print('num1:', id(self.num1), 'num2:', id(self.num2))
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

def printResult(objName, obj):
    print(objName + '.add:', obj.add())
    print(objName + '.sub:', obj.sub())
    print(objName + '.mul:', obj.mul())
    print(objName + '.div:', obj.div())

print('<c1>')
c1 = Calc(10, 20)
c1.setData(100, 50)
c1.setData(5000, 2000) # setData를 호출할 때마다 c1.num1, c1.num2의 참조가 달라진다. (같은 참조, 다른 값이 아니라)
printResult('c1', c1)
print()

print('<c2>')
c2 = Calc(34.772, 25.91)
printResult('c2', c2)
print()
