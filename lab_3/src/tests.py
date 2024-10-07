from algs import *

def testing():
    print("\nLINEAR SEARCH TEST:")
    test_func(linear_search)
    print("\nBINARY SEARCH TEST:")
    test_func(binary_search)


def test_func(func):
    # TEST 1
    arr = []
    x = 1
    res = -1
    print("TEST 1 IS OK") if func(arr, x)[0] == res else print("ERROR 1 TEST INCORRECT")

    # TEST 2
    arr = [1]
    x = 2
    res = -1
    print("TEST 2 IS OK") if func(arr, x)[0] == res else print("ERROR 2 TEST INCORRECT")

    # TEST 3
    arr = [1, 2, 3, 4, 5]
    x = 0
    res = -1
    print("TEST 3 IS OK") if func(arr, x)[0] == res else print("ERROR 3 TEST INCORRECT")

    # TEST 4
    arr = [1, 2, 3, 4, 5]
    x = 1
    res = 1
    print("TEST 4 IS OK") if func(arr, x)[0] == res else print("ERROR 4 TEST INCORRECT")

    # TEST 5
    arr = [1, 2, 3, 4, 5]
    x = 2
    res = 2
    print("TEST 5 IS OK") if func(arr, x)[0] == res else print("ERROR 5 TEST INCORRECT")

    # TEST 6
    arr = [1, 2, 3, 4, 5]
    x = 3
    res = 3
    print("TEST 6 IS OK") if func(arr, x)[0] == res else print("ERROR 6 TEST INCORRECT")

    # TEST 7
    arr = [1, 2, 3, 4, 5]
    x = 4
    res = 4
    print("TEST 7 IS OK") if func(arr, x)[0] == res else print("ERROR 7 TEST INCORRECT")

    # TEST 8
    arr = [1, 2, 3, 4, 5]
    x = 5
    res = 5
    print("TEST 8 IS OK") if func(arr, x)[0] == res else print("ERROR 8 TEST INCORRECT")

    # TEST 9
    arr = [1, 2, 3, 4, 5]
    x = 6
    res = -1
    print("TEST 9 IS OK") if func(arr, x)[0] == res else print("ERROR 9 TEST INCORRECT")

    # TEST 10
    arr = [1, 2, 3, 4]
    x = 4
    res = 4
    print("TEST 10 IS OK") if func(arr, x)[0] == res else print("ERROR 10 TEST INCORRECT")

    # TEST 11
    arr = [1, 2, 3, 4]
    x = 1
    res = 1
    print("TEST 11 IS OK") if func(arr, x)[0] == res else print("ERROR 11 TEST INCORRECT")

    # TEST 12
    arr = [1, 2, 3, 4]
    x = 0
    res = -1
    print("TEST 12 IS OK") if func(arr, x)[0] == res else print("ERROR 12 TEST INCORRECT")


if __name__ == '__main__':
    testing()