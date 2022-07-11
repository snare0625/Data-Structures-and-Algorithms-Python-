def factorial(n):
    assert n>=0 and int(n) == n, 'This number must be positive integer only'
    if n in [0, 1]:
        return n
    else:
        return n*factorial(n-1)

print(factorial(995))