#s = input("콤마없이 a b c 입력: ")
#strList = s.split()
#print(strList)
#floatList = [float(i) for i in strList]
#print(floatList)
for i in range(1,4):
    a,b,c = eval(input("콤마를 사용해서 a,b,c 입력: "))
    d = b**2 - 4 * a * c
    if d > 0:
        r1 = (-b - d**0.5) / 2*a
        r2 = (-b + d ** 0.5) / 2 * a
        print("실근은 {0:.2f},{1:.2f} 입니다".format(r1,r2))
    elif d == 0:
        r1 = - b / 2*a
        print("실근은 {0:.2f} 입니다".format(r1))
    else:
        r1 = -b / 2*a
        print("실근은 없습니다.")