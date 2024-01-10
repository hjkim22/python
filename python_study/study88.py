def open_account():
    print("새로운 계좌 생성")

def deposit(balance, money):
    print("입금이 완료되었습니다. 입금 금액은 {}원, 현재 잔액은 {}원입니다.".format(money, balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 출금 금액은 {}원, 현재 잔액은 {}원입니다.".format(money, balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 출금 시도 금액은 {}원, 현재 잔액은 {}원입니다.".format(money, balance))
        return balance
    
def withdraw_night(balance, money):
    commission = 500
    if balance >= money + commission:
        print("출금이 완료되었습니다. 출금 금액은 {}원, 수수료는 {}원, 현재 잔액은 {}원입니다.".format(money, commission, balance - money - commission))
    elif balance < money + commission:
        print("출금이 완료되지 않았습니다. 현재 잔액은 {}원입니다.".format(balance))


balance = 0
balance = deposit(balance, 10000)
# balance = withdraw(balance, 500)
# balance = withdraw(balance, 2200)
# balance = withdraw_night(balance, 20000)
balance = withdraw_night(balance, 9500)