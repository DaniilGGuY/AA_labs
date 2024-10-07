from algs import *

def testing():
    print("\nSTANDARD ALGORITHM TEST:")
    test_func(standard_mult)
    print("\nVINOGRAD ALGORITHM TEST:")
    test_func(vinograd_alg)
    print("\nOPTIMIZED VINOGRAD ALGORITHM TEST:")
    test_func(optimized_vinograd_alg)


def test_func(func):
    # TEST 1
    A = [[]]
    B = [[]]
    C = []
    print("TEST 1 IS OK") if func(A, B) == C else print("ERROR 1 TEST INCORRECT")

    # TEST 2
    A = [[1]]
    B = [[2]]
    C = [[2]]
    print("TEST 2 IS OK") if func(A, B) == C else print("ERROR 2 TEST INCORRECT")

    # TEST 3
    A = [[1, 2]]
    B = [[2],
         [1]]
    C = [[4]]
    print("TEST 3 IS OK") if func(A, B) == C else print("ERROR 3 TEST INCORRECT")

    # TEST 4
    A = [[1, 2]]
    B = [[2]]
    C = []
    print("TEST 4 IS OK") if func(A, B) == C else print("ERROR 4 TEST INCORRECT")

    # TEST 5
    A = [[1],
         [2]]
    B = [[2, 1]]
    C = [[2, 1],
         [4, 2]]
    print("TEST 5 IS OK") if func(A, B) == C else print("ERROR 5 TEST INCORRECT")

    # TEST 6
    A = [[1, 2, 3],
         [3, 2, 1]]
    B = [[2, 1],
         [3, 0],
         [4, 2]]
    C = [[20, 7],
         [16, 5]]
    print("TEST 6 IS OK") if func(A, B) == C else print("ERROR 6 TEST INCORRECT")

    # TEST 7
    A = [[1, 2, 3],
         [4, 5, 6]]
    B = [[1],
         [2],
         [3]]
    C = [[14],
         [32]]
    print("TEST 7 IS OK") if func(A, B) == C else print("ERROR 7 TEST INCORRECT")

    # TEST 8
    A = [[1, 1],
         [1, 1]]
    B = [[1, 1],
         [1, 1]]
    C = [[2, 2],
         [2, 2]]
    print("TEST 8 IS OK") if func(A, B) == C else print("ERROR 8 TEST INCORRECT")

    # TEST 9
    A = [[1, 0],
         [0, 1]]
    B = [[-1, 0],
         [0, -1]]
    C = [[-1, 0],
         [0, -1]]
    print("TEST 9 IS OK") if func(A, B) == C else print("ERROR 9 TEST INCORRECT")

    # TEST 10
    A = [[1, 0],
         [0, 1]]
    B = [[0, 0],
         [0, 0]]
    C = [[0, 0],
         [0, 0]]
    print("TEST 10 IS OK") if func(A, B) == C else print("ERROR 10 TEST INCORRECT")

if __name__ == '__main__':
    testing()
