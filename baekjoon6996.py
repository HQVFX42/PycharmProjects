TestCase = eval(input())
for i in range(TestCase):
    strList =  input().split()
    first = []
    first += strList[0]
    second = []
    second += strList[1]
    first.sort()
    second.sort()
    flag = True
    if len(first) == len(second):
        for j in range(len(first)):
            if first[j] != second[j]:
                flag = False
    else:
        flag = False
    if flag:
        print("{0} & {1} are anagrams.".format(strList[0],strList[1]))
    else:
        print("{0} & {1} are NOT anagrams.".format(strList[0], strList[1]))