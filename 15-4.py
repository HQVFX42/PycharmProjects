def m(i):
    if i == 1:
        return 1
    else:
        return 1/i + m(i-1)

for i in range(1, 11):
    print("m(", i,")=",m(i))


