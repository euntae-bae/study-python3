# 예제8: 정적 메서드
class Calc:
    @staticmethod       # 정적 메서드에는 @staticmethod 데코레이터를 표시한다.
    def add(a, b):      # 정적 메서드는 self를 매개변수로 사용하지 않는다.
        return a + b
    
    @staticmethod
    def sub(a, b):
        return a - b
    
    @staticmethod
    def mul(a, b):
        return a * b
    
    @staticmethod
    def div(a, b):
        return a / b
