# 예제4: 클래스 변수
class Account:
    # 클래스 변수 nAccounts
    nAccounts = 0
    # 생성자
    def __init__(self, name):
        self.name = name
        Account.nAccounts += 1
    # 소멸자
    def __def__(self):
        Account.nAccounts -= 1

acc1 = Account('Kim')
acc2 = Account('Lee')
acc3 = Account('Park')
print(acc1.name)            # Kim
print(acc1.nAccounts)       # 3
print(acc2.name)            # Lee
print(acc2.nAccounts)       # 3
print(Account.nAccounts)    # 3
