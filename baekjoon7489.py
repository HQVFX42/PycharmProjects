def rightmostnonzerodigit(n, count):
    while True:
        if n % 10 > 0 :
            return n % pow(10, count)
        else:
            n=n // 10

def fact(n):
    result = 1
    for i in range(1, n+1):
        result = rightmostnonzerodigit(result *i, 10)
    print(rightmostnonzerodigit(result, 1))

fact(1000)