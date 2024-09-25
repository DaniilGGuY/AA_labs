from algs import recursive_alg, DP_alg, damerau_alg, cache_alg
from tests import testing
from reserch import research

while True:
    print("Меню:")
    print("1 - Тестирование программы")
    print("2 - Ручной ввод строк")
    print("3 - Провести исследование алгоритмов")
    print("0 - Завершить программу")
    a = int(input("Введите номер команды: "))
    if a == 0:
        break
    elif a == 1:
        testing()
    elif a == 2:
        s1 = input("Первая строка: ")
        s2 = input("Вторая строка: ")

        print("Рекурсивный алгоритм говорит, что расстояние равно: ", recursive_alg(s1, s2))
        print("Алгоритм основанный на ДП говорит, что расстояние равно: ", DP_alg(s1, s2))
        print("Алгоритм Дамерау-Левенштейна говорит, что расстояние равно: ", damerau_alg(s1, s2))
        print("Рекурсивный алгоритм с кэширование говорит, что расстояние равно: ",
              cache_alg(s1, s2, [[-1 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]))
    elif a == 3:
        research()
