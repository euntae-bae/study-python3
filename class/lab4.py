# 예제4: 클래스 변수
class Account:
    # 클래스 변수 nAccounts
    nAccounts = 0
    # 생성자
    def __init__(self, name):
        self.name = name
        Account.nAccounts += 1
    # 소멸자
    def __del__(self):
        Account.nAccounts -= 1
        print('Account.nAccounts: ', Account.nAccounts)

acc1 = Account('Kim')
acc2 = Account('Lee')
acc3 = Account('Park')
print(acc1.name)            # Kim
print(acc1.nAccounts)       # 3
print(acc2.name)            # Lee
print(acc2.nAccounts)       # 3
del acc1
del acc2

print(acc3.name)            # Park
print(Account.nAccounts)    # 1
