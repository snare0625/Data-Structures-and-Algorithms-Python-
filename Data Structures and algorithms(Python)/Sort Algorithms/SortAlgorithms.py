#Merges two arrays of custom list
def merge(customList, l, m, r):
    #number of elements in firstSubArray
    n1 = m - l + 1
    n2 = r - m

    #Two temp array
    L = [0] * (n1)
    R = [0] * (n2)

    #Copy elements from customList to the subArrays
    #1st subArrays
    for i in range(0, n1):
        L[i] = customList[i + l]

    for j in range(0, n2):
        R[j] = customList[m+1+j]

    #Merge the two sub arrays
    i = 0
    j = 0
    k = 0
    while i < n1:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    #Add remaining elements to newly Sorted list
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        i += 1
        k += 1

def mergeSort(customList, l, m, r):
    if l < r:
        m = (l+(r - 1)) //2
        mergeSort(customList, l, r)
        mergeSort(customList, m+1, r)
        merge(customList, l, m, r)

#DRIVER CODE
cList = [2, 1, 2, 7, 6, 5, 4 ,3, 9]
print(mergeSort(cList, 0, 9))