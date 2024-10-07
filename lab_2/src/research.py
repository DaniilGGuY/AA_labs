import matplotlib.pyplot as plt
import time
from algs import *

def research():
    col_measure = 100
    sizes = [20 * i for i in range(1, 6)]
    std_alg_t = list()
    vin_alg_t = list()
    opt_vin_alg_t = list()
    for i in sizes:
        mat_1 = [[0] * i for j in range(i)]
        mat_2 = [[0] * i for j in range(i)]

        begin = time.process_time()
        #begin = time.ticks_ms()
        for j in range(col_measure):
            standard_mult(mat_1, mat_2)
        #end = time.ticks_ms()
        end = time.process_time()
        std_alg_t.append((end - begin) / col_measure)

        begin = time.process_time()
        #begin = time.ticks_ms()
        for j in range(col_measure):
            vinograd_alg(mat_1, mat_2)
        #end = time.ticks_ms()
        end = time.process_time()
        vin_alg_t.append((end - begin) / col_measure)

        begin = time.process_time()
        #begin = time.ticks_ms()
        for j in range(col_measure):
            optimized_vinograd_alg(mat_1, mat_2)
        #end = time.ticks_ms()
        end = time.process_time()
        opt_vin_alg_t.append((end - begin) / col_measure)

    print(std_alg_t)
    print(vin_alg_t)
    print(opt_vin_alg_t)
    fig = plt.subplots(figsize=(10, 8))
    plt.title("Сравнение по времени")
    plt.xlabel("Размер строки квадратной матрицы")
    plt.ylabel("Время выполнения в секундах")
    plt.plot(sizes, std_alg_t, label="Стандартный алгоритм")
    plt.plot(sizes, vin_alg_t, label="Алгоритм Винограда")
    plt.plot(sizes, opt_vin_alg_t, label="Оптимизированный алгоритм")
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    research()