def m(i):
    if i == 1:
        return i/(i+1)
    else:
        return i/(i+1) + m(i-1)

for i in range(1, 21):
    print("m(", i,")=",m(i))
