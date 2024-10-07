from algs import linear_search, binary_search
from tests import testing
from research import research

while True:
    print("Меню:")
    print("1 - Тестирование программы")
    print("2 - Ручной ввод")
    print("3 - Провести исследование алгоритмов")
    print("0 - Завершить программу")
    a = int(input("Введите номер команды: "))
    if a == 0:
        break
    elif a == 1:
        testing()
    elif a == 2:
        n = int(input("Введите размер целочисленного массива: "))
        arr = [0] * n
        for i in range(n):
            arr[i] = int(input(f'Введите {i + 1}-ый элемент массива: '))

        while True:
            try:
                x = int(input("Введите элемент, который надо найти: "))
            except ValueError:
                break

            ind_l, comp_l = linear_search(arr, x)
            print("Искомый массив: ", *arr)
            if ind_l == -1:
                print(f'Заданный элемент {x} не найден линейным поиском. Выполнено {comp_l} сравнений')
            else:
                print(f'Линейный поиск нашел элемент {x} на позиции {ind_l} за {comp_l} сравнений')

            arr2 = sorted(arr)
            ind_b, comp_b = binary_search(arr2, x)
            print("Искомый массив: ", *arr2)
            if ind_b == -1:
                print(f'Заданный элемент {x} не найден бинарным поиском. Выполнено {comp_b} сравнений')
            else:
                print(f'Бинарный поиск нашел элемент {x} на позиции {ind_b} за {comp_b} сравнений')

    elif a == 3:
        research()
