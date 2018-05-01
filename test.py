str = input("10개의 숫자를 입력하세요: ")
stringList = str.split()
list1 = []
list2 = []
for i in stringList:
    list1.append(eval(i))
for j in list1:
    if not j in list2:
        list2.append(j)
print("중복을  제거한 고유한 숫자: ",end="")
for j in list2:
    print(j, end=" ")
