class reverse:
    def __init__(self,N,K):
        self.N = N
        self.K = K
    def getN(self):
        return self.N
    def getK(self):
        return self.K
    def reverseProgram(self,number):
        result = 0
        while number > 0 :
            result = result * 10 + number % 10
            number //= 10
        return result

def reverseP(number):
    result = 0
    while number > 0:
        result = result*10 + number % 10
        number //= 10
    return result

strList = input().split()
N = int(strList[0])
K = int(strList[1])
High = 0
for i in range(1, K+1):
    num = reverseP(N*i)
    if High < num:
        High = num
print(High)