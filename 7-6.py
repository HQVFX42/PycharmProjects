class QuardraticEquation:
    def __init__(self,a,b,c):
        self.__a = a
        self.__b = b
        self.__c = c
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getDiscriminant(self):
        return self.__b**2 - 4*self.__a*self.__c
    def getRoot1(self):
        if self.getDiscriminant() >= 0:
            return (-self.__b + self.getDiscriminant()**0.5) / 2*self.__a
        else:
            return 0
    def getRoot2(self):
        if self.getDiscriminant() >= 0:
            return (-self.__b - self.getDiscriminant()**0.5) / 2*self.__a
        else:
            return 0
a,b,c = eval(input("a,b,c를 콤마 구분해서 입력하세요: "))
q = QuardraticEquation(a,b,c)
if q.getDiscriminant() > 0:
    print("두 실근 {0:.2f}, {1:.2f}".format(q.getRoot1(),q.getRoot2()))
elif q.getDiscriminant() == 0:
    print("중근 {0:2f}", format(q.getRoot1()))
else:
    print("해는 없습니다")