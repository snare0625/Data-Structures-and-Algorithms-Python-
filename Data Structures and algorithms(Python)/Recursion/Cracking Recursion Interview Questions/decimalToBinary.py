def decimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return n
    return n%2 + 10*decimalToBinary(int(n/2))

print(decimalToBinary(10))

print("Neo"[1:-1])