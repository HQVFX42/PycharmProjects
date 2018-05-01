def isAnagram(s1, s2):
    for i in range(len(s1)):
        strList1 = s1.split()
        strList2 = s2.split()
        first = []
        first += strList1[0]
        second = []
        second += strList2[0]
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
            return True
        else:
            return False

s1 = input("첫번째 영단어: ")
s2 = input("두번째 영단어: ")
print(s1, "와", s2, "는", end=" ")
if isAnagram(s1, s2):
    print("애너그램")
else:
    print("Not 애너그램")