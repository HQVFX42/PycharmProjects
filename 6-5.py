def displaySortedNumbers(num1, num2, num3):
    l = [num1, num2, num3]
    l.sort()
    print(l)

n1, n2, n3 = eval(input("숫자 3개 입력:"))
displaySortedNumbers(n1, n2, n3)

