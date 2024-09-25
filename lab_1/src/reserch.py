import matplotlib.pyplot as plt
import time
from algs import *
import string
import random

def generate_random_string(size):
    return ''.join(random.choices(string.ascii_letters, k=size))


def research():
    col_measure = 150
    sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rec_alg_l = list()
    rec_alg_cache_l = list()
    dp_alg_l = list()
    damerau_alg_l = list()
    for i in sizes:
        s1_l = list()
        s2_l = list()
        for j in range(col_measure):
            s1_l.append(generate_random_string(i))
            s2_l.append(generate_random_string(i))

        begin = time.process_time()
        for j in range(col_measure):
            recursive_alg(s1_l[j], s2_l[j])
        end = time.process_time()
        rec_alg_l.append((end - begin) / col_measure)

        mat = [[[-1 for i in range(len(s2_l[j]) + 1)] for j in range(len(s1_l[j]) + 1)] for k in range(col_measure)]
        begin = time.process_time()
        for j in range(col_measure):
            cache_alg(s1_l[j], s2_l[j], mat[j])
        end = time.process_time()
        rec_alg_cache_l.append((end - begin) / col_measure)

        begin = time.process_time()
        for j in range(col_measure):
            DP_alg(s1_l[j], s2_l[j])
        end = time.process_time()
        dp_alg_l.append((end - begin) / col_measure)

        begin = time.process_time()
        for j in range(col_measure):
            damerau_alg(s1_l[j], s2_l[j])
        end = time.process_time()
        damerau_alg_l.append((end - begin) / col_measure)

    print(rec_alg_l)
    print(rec_alg_cache_l)
    print(dp_alg_l)
    print(damerau_alg_l)
    fig = plt.subplots(figsize=(10, 8))
    plt.title("Сравнение по времени")
    plt.xlabel("Размер строки")
    plt.ylabel("Время выполнения")
    plt.plot(sizes, rec_alg_l, label="Рекурсивный")
    plt.plot(sizes, rec_alg_cache_l, label="Рекурсивный + кэш")
    plt.plot(sizes, dp_alg_l, label="Нерекурсивный")
    plt.plot(sizes, damerau_alg_l, label="Нерекурсивный + Дамерау")
    plt.legend(loc='upper left')
    plt.show()