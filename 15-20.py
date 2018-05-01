def decimalToHex1(value):
    if value == 0:
        return ""
    else:
        r = value % 16
        if r >= 10:
            temp = chr(ord('A') + r - 10)
        else:
            temp = str(r)
        return decimalToHex1(value//16)+ temp


def decimalToHex2(value):
    number = "0123456789ABCDEF"
    if value == 0:
        return ""
    else:
        r = value % 16
        return decimalToHex2(value // 16) + number[r]

value = eval(input("10진수 입력: "))
print(value, "을 16진수로 바꾸면", decimalToHex2(value))