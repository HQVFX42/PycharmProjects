def Average(n):
    result = 0
    for i in range(1, n+1):
        result += result
    return result

Average(1)