def program(n):
    result = 0
    for i in range(1, n):
        result += n *i + i

    print(result)

n = int(input())
program(n)