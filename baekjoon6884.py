def isPrimeNumber(n):
    seive = [False, False] + [True] * (n-1)
    for (i, e) in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return [x for (x,y) in enumerate(seive) if y]

def Numbers(length, intList):
    for i in range(len(intList) - length + 1):
        result = []
        for j in range(i, i + length):
            result.append(intList[j])
        if isPrimeNumber(sum(result)):
            return result
    return []

TestCase = eval(input())
for i in range(TestCase):
    strList = input().split()
    intList = [eval(i) for i in strList]
    intList.pop(0)
    flag = True
    for j in range(2, len(intList) + 1):
        result = Numbers(j, intList)
        if len(result) > 0 :
            print("Shortest primes subsequence is length {0}: ".format(j))
            for k in result:
                print("{0}".format(k), end=" ")
            print()
            flag = False
            break
    if flag:
            print("This sequence is anti-primed.")