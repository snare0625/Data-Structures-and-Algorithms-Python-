def maxProduct(array):
    array.sort()
    n = len(array)
    print(array[n-1]*array[n-2])
    print(array[n-1], array[n-2])

maxProduct([1, -2, 3, -4])

def max2(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[j]*array[i] > maxProduct:
                maxProduct = array[i]*array[j]
                print(maxProduct)
                print(array[i], array[j])

