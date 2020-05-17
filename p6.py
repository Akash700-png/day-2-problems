def is_odd(n):
    if n%2 == 0:
        return False
    return True
def is_prime(n):
    x = 2
    y = n//2
    while y>=x:
        if n%x == 0:
            return False
        x = x+1
        y =n//x
    return True
def is_palindrom(n):
    m = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    if m == rev:
        return True
    return False
def is_armstrong(n):
    m = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev + rem * rem * rem
        n = n // 10
    if m == rev:
        return True
    return False

def check():
    number = int(input("Enter the number :"))
    if(is_odd(number)):
        print(number," is a odd number :")
    else:
        print(number," is a even number :")
    if(is_prime(number)):
        print(number," is a prime number :")
    if(is_palindrom(number)):
        print(number," is a palindrom number :")
    if(is_armstrong(number)):
        print(number," is an armstrong number :")

check()


