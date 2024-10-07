def linear_search(arr, x):
    if len(arr) == 0:
        return -1, 0

    compares = 0
    for ind, i in enumerate(arr):
        compares += 1
        if i == x:
            return ind + 1, compares

    return -1, compares

def binary_search(arr, x):
    if len(arr) == 0:
        return -1, 0

    compares = 0
    lhs = 0
    rhs = len(arr)
    while lhs < rhs - 1:
        compares += 1
        mid = (rhs + lhs) // 2
        if arr[mid] == x:
            return mid + 1, compares
        elif arr[mid] < x:
            lhs = mid
        else:
            rhs = mid

    compares += 1
    if arr[lhs] != x:
        return -1, compares

    return lhs + 1, compares