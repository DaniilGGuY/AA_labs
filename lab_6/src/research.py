from inout import random_mat
from standard import standard_alg
from ant import ant_alg
from time import process_time
import matplotlib.pyplot as plt

def research():
    col_measure = 10
    sizes = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    standart_t = list()
    ant_t = list()
    alpha, ro, t_max = 0.1, 0.1, 200
    for size in sizes:
        mat = random_mat(size)
        beg = process_time()
        for i in range(col_measure):
            standard_alg(mat)
        end = process_time()
        standart_t.append((end - beg) / col_measure)

        beg = process_time()
        for i in range(col_measure):
            ant_alg(mat, alpha, ro, t_max)
        end = process_time()
        ant_t.append((end - beg) / col_measure)

    print(standart_t)
    print(ant_t)
    fig = plt.subplots(figsize=(10, 8))
    plt.title("Сравнение по времени")
    plt.xlabel("Количество узлов")
    plt.ylabel("Время выполнения в секундах")
    plt.plot(sizes, standart_t, label="Полный перебор")
    plt.plot(sizes, ant_t, label="Муравьиный алгоритм")
    plt.legend(loc='upper left')
    plt.show()