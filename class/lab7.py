# 예제7: 생성자에서 리스트 초기화
class InstanceVar:
    def __init__(self):
        self.textList = []

    def add(self, text):
        self.textList.append(text)
    
    def printList(self):
        print(self.textList)

if __name__ == '__main__':
    a = InstanceVar()
    a.add('hello')  # ['hello']
    a.printList()

    b = InstanceVar()
    b.add('world')
    b.printList()   # ['world']