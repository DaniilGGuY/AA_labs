from inout import input_mat, random_mat, input_coefs, output_mat
from standard import standard_alg
from ant import ant_alg
from research import research
from tests import testing

while True:
    print("Меню:")
    print("1 - Тестирование программы")
    print("2 - Ручной ввод матрицы смежности")
    print("3 - Автоматическая генерация матрицы смежности")
    print("4 - Провести исследование алгоритмов")
    print("0 - Завершить программу")
    a = int(input("Введите номер команды: "))
    if a == 0:
        break
    elif a == 1:
        testing()
    elif a == 2:
        mat = input_mat()
        alpha, ro, t_max = input_coefs()
        min_path_std, min_len_std = standard_alg(mat)
        print("Ответ, полученный с помощью полного перебора: ", min_path_std)
        print("Длина пути равна: ", min_len_std)
        min_path_ant, min_len_ant = ant_alg(mat, alpha, ro, t_max)
        print("Ответ, полученный с помощью муравьев: ", min_path_ant)
        print("Длина пути равна: ", min_len_ant)
    elif a == 3:
        n = int(input("Введите количество вершин в графе: "))
        mat = random_mat(n)
        print("Полученная матрица расстояний:")
        output_mat(n, mat)
        alpha, ro, t_max = input_coefs()
        min_path_std, min_len_std = standard_alg(mat)
        print("Ответ, полученный с помощью полного перебора: ", min_path_std)
        print("Длина пути равна: ", min_len_std)
        min_path_ant, min_len_ant = ant_alg(mat, alpha, ro, t_max)
        print("Ответ, полученный с помощью муравьев: ", min_path_ant)
        print("Длина пути равна: ", min_len_ant)
    elif a == 4:
        research()
