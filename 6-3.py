def reverse(number):
    result = 0
    while number > 0:
        result = result * 10 + (number % 10)
        number //= 10
        print(result, number)
    return result

def isPalindrome(number):
    if number == reverse(number):
        print("True")
    else:
        print("False")

isPalindrome(456)
isPalindrome(121)