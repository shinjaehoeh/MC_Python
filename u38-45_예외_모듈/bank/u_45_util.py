class Account:
    def __init__(self, acno, own, bal):
     self.acno = acno
     self.own = own
     self.__bal = bal

    def __str__(self):
       return f'num:{self.acno}, owner:{self.own}, bal:{self.__bal}'

    def deposit(self,money):
        if money + self.__bal <= 1000:
            self.__bal += money
        else :
            print("u can't")

    def withdraw(self,money):
        if self.__bal - money < 0:
         print('no')
         return
        self.__bal -= money