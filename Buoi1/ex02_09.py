def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số: "))

if IsPrime(n):
    print(n,"là số nguyên tố!")
else:
    print(n,"không là số nguyên tố!")