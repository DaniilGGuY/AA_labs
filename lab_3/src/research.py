import matplotlib.pyplot as plt
from algs import *
import random

VARIANT = 1028

def research():
    arr = random.sample(range(10000), VARIANT)
    linear_arr_comps = [0] * VARIANT
    for i in range(VARIANT):
        linear_arr_comps[i] = linear_search(arr, arr[i])[1]

    arr2 = sorted(arr)
    binary_sort_arr_comps = [0] * VARIANT
    for i in range(VARIANT):
        binary_sort_arr_comps[i] = binary_search(arr2, arr[i])[1]


    fig = plt.subplots(figsize=(8, 4))
    plt.xlabel("Позиция элементов в массиве")
    plt.ylabel("Количество сравнений")
    plt.bar([i for i in range(VARIANT)], linear_arr_comps)
    #plt.bar([i for i in range(VARIANT)], binary_sort_arr_comps)
    #plt.bar([i for i in range(VARIANT)], sorted(binary_sort_arr_comps))
    plt.show()


if __name__ == '__main__':
    research()