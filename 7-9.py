class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def getA(self):
        return self.__a
    def getB(self):
        return self.__b
    def getC(self):
        return self.__c
    def getD(self):
        return self.__d
    def getE(self):
        return self.__e
    def getF(self):
        return self.__f
    def isSolvable(self):
        if ((self.__a*self.__d) - (self.__b*self.__c)) == 0:
            return False
        else:
            return True
    def getX(self):
        if self.isSolvable() == True:
            return ((self.__e*self.__d) - (self.__b*self.__f)) / ((self.__a*self.__d) - (self.__b*self.__c))
    def getY(self):
        if self.isSolvable() == True:
            return ((self.__a*self.__f) - (self.__e * self.__c)) / ((self.__a*self.__d) - (self.__b*self.__c))


x1,y1,x2,y2 = eval(input("첫번째 성분의 양 끝점을 입력하세요: "))
x3,y3,x4,y4 = eval(input("두번째 성분의 양 끝점을 입력하세요: "))
l = LinearEquation(x2-x1, -(y2-y1), x4-x3, -(y4-y3), (x2-x1)*x1 + -((y2-y1) * y1), (x4-x3)*x3 + -((y4-y3)*y3) )

if l.isSolvable() == False:
    print("해는 없습니다")
else:
    print("x = {0:.2f}, y = {1:.2f}".format(l.getX(),l.getY()))