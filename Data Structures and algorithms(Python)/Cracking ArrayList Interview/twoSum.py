def pairSum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j] == target:
                return [i, j]

print(pairSum([1, 2, 3, 5], 8))