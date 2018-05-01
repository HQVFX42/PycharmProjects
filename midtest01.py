class class1:
    def __init__(self, number):
        self.__number = number
    def func(self):
        result = 0
        num1 = self.__number % 10
        num2 = self.__number // 10  % 10
        num3 = self.__number // 10 // 10 % 10
        print("백의자리 : ", num3)
        print("십의자리 : ", num2)
        print("일의자리 : ", num1)


n = int(input("숫자입력: "))
c1 = class1(n)
c1.func()