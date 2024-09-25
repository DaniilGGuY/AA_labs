from algs import *

def testing():
    print("Тестируем рекурсивный алгоритм:")
    print("Test1 OK") if recursive_alg("а", "") == 1 else print("ERROR")
    print("Test2 OK") if recursive_alg("", "") == 0 else print("ERROR")
    print("Test3 OK") if recursive_alg("а", "б") == 1 else print("ERROR")
    print("Test4 OK") if recursive_alg("а", "аб") == 1 else print("ERROR")
    print("Test5 OK") if recursive_alg("река", "мука") == 2 else print("ERROR")
    print("Test6 OK") if recursive_alg("реак", "мука") == 4 else print("ERROR")
    print("Test7 OK") if recursive_alg("морковка", "сосиска") == 5 else print("ERROR")
    print("Test8 OK") if recursive_alg("мамам", "мамам") == 0 else print("ERROR")

    print("\nТестируем нерекурсивный алгоритм:")
    print("Test1 OK") if DP_alg("а", "") == 1 else print("ERROR")
    print("Test2 OK") if DP_alg("", "") == 0 else print("ERROR")
    print("Test3 OK") if DP_alg("а", "б") == 1 else print("ERROR")
    print("Test4 OK") if DP_alg("а", "аб") == 1 else print("ERROR")
    print("Test5 OK") if DP_alg("река", "мука") == 2 else print("ERROR")
    print("Test6 OK") if DP_alg("реак", "мука") == 4 else print("ERROR")
    print("Test7 OK") if DP_alg("морковка", "сосиска") == 5 else print("ERROR")
    print("Test8 OK") if DP_alg("мамам", "мамам") == 0 else print("ERROR")

    print("\nТестируем рекурсивный алгоритм c кэшированием:")
    print("Test1 OK") if cache_alg("а", "",
          [[-1 for i in range(1)] for j in range(2)]) == 1 else print("ERROR")
    print("Test2 OK") if cache_alg("", "",
          [[-1 for i in range(1)] for j in range(1)]) == 0 else print("ERROR")
    print("Test3 OK") if cache_alg("а", "б",
          [[-1 for i in range(2)] for j in range(2)]) == 1 else print("ERROR")
    print("Test4 OK") if cache_alg("а", "аб",
          [[-1 for i in range(3)] for j in range(2)]) == 1 else print("ERROR")
    print("Test5 OK") if cache_alg("река", "мука",
          [[-1 for i in range(5)] for j in range(5)]) == 2 else print("ERROR")
    print("Test6 OK") if cache_alg("реак", "мука",
          [[-1 for i in range(5)] for j in range(5)]) == 4 else print("ERROR")
    print("Test7 OK") if cache_alg("морковка", "сосиска",
          [[-1 for i in range(8)] for j in range(9)]) == 5 else print("ERROR")
    print("Test8 OK") if cache_alg("мамам", "мамам",
          [[-1 for i in range(6)] for j in range(6)]) == 0 else print("ERROR")

    print("\nТестируем нерекурсивный алгоритм Дамерау-Левенштейна:")
    print("Test1 OK") if damerau_alg("а", "") == 1 else print("ERROR")
    print("Test2 OK") if damerau_alg("", "") == 0 else print("ERROR")
    print("Test3 OK") if damerau_alg("а", "б") == 1 else print("ERROR")
    print("Test4 OK") if damerau_alg("а", "аб") == 1 else print("ERROR")
    print("Test5 OK") if damerau_alg("река", "мука") == 2 else print("ERROR")
    print("Test6 OK") if damerau_alg("реак", "мука") == 3 else print("ERROR")
    print("Test7 OK") if damerau_alg("морковка", "сосиска") == 5 else print("ERROR")
    print("Test8 OK") if damerau_alg("мама", "амам") == 2 else print("ERROR")
    print("Test9 OK") if damerau_alg("мамам", "мамам") == 0 else print("ERROR")