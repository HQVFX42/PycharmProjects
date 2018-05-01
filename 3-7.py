import time
def Change(number):
    result = 0
    result =  65 + (number % 25)
    #print(result)
    print("출력된 문자 : ",chr(result))

strT = time.time()
a = int(strT)
Change(a)
strT2 = time.time()
b = int(strT)+35
Change(b)
