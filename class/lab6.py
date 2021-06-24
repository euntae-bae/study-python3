# 예제6: __new__()와 __init__()
# __new__(): 클래스 인스턴스를 메모리에 할당해 "생성" -> allocator, instantiator
# __init__(): "생성"된 인스턴스를 "초기화" -> constructor, initializer
# __new__()는 할당자(allocator)로, 클래스 메서드다. 반면, __init__()은 생성자(constructor)로, 인스턴스 메서드다.
# 객체의 메모리 할당은 __init__()이 아니라 __new__()에서 수행된다.
# 엄밀하게 따지면 파이썬의 __new__(), __init__() 모두 C++나 자바에서 말하는 생성자와는 다르다. 다만 유사한 작업을 수행할 뿐이다.
# __new__()를 직접 수정하는 경우는 거의 없다.
class Foo:
    @staticmethod
    def bar(n):
        return n * 5
    def __new__(cls, n):
        return Foo.bar(n)

print(Foo(3)) # 15
print(type(Foo(5))) # <class 'int'>
