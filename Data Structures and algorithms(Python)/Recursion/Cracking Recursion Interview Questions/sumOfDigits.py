def sumOfDigits(n):
    assert n>=0 and int(n) == n, 'This has to be a positive integer only'
    if n == 0:
        return n
    else:
        return n%10 + sumOfDigits(int(n/10))


print(sumOfDigits(12))
