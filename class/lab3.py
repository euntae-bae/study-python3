# 예제3: 가설 - 파이썬의 모든 변수는 값이 아니라 참조를 저장하는가?
num1 = 1000
print('id(num1):', id(num1))
num1 = 5000
print('id(num1):', id(num1))
num2 = 1010
num1 = num2
print('id(num1):', id(num1), 'id(num2):', id(num2))
print('num1 is num2:', num1 is num2)
# num1과 num2는 서로 같은 값을 갖는 다른 객체가 아니라, 같은 객체를 가리키는 다른 참조변수라고 할 수 있다.