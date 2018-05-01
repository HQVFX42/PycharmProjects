r = int(input("연이율 입력(예. 3%는 3):"))
a = int(input("매달 저축할 금액:"))

monthrate = r/100 / 12
#result = a * (1+month)


for i in range(1, 13):
    result = 0
    result = (a)*(1+monthrate)
    print(i, int(result*100) / 100)
    a = a + result