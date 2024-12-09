from inout import random_mat, input_mat_from_file
from standard import standard_alg
from ant import ant_alg

MAX_ITERS = 10

def generate():
    file = open("../data/3.txt", "w")
    mat = random_mat(10)
    for i in mat:
        file.write(" ".join(map(str, i)) + '\n')
    file.close()

def testing():
    files = ["../data/1.txt", "../data/2.txt", "../data/3.txt"]
    ans = [([5, 1, 6, 2, 4, 8, 3, 7], 25), ([9, 8, 2, 5, 3, 6, 7, 4, 1], 24), ([5, 3, 1, 6, 9, 7, 4, 10, 2, 8], 36)]
    print("Тестируется стандартный алгоритм...")
    mats = list()
    for i, file in enumerate(files):
        mats.append(input_mat_from_file(file))
        if standard_alg(mats[i]) == ans[i]:
            print(f"СТАНДАРТНЫЙ АЛГОРИТМ: ТЕСТ {i + 1}, СТАТУС: OK")
        else:
            print(f"СТАНДАРТНЫЙ АЛГОРИТМ: ТЕСТ {i + 1}, СТАТУС: ERROR")

    for alpha in [0.1, 0.25, 0.5, 0.75, 0.9]:
        for ro in [0.1, 0.25, 0.5, 0.75, 0.9]:
            print("\\hline")
            for tmax in [200, 500, 1000, 1500, 2000]:
                str = f"{alpha} & {ro} & {tmax}"
                for i in range(3):
                    min_d, max_d, mean_d, sum_d = -1, -1, -1, 0
                    for it in range(MAX_ITERS):
                        ans_length = ans[i][1]
                        length = ant_alg(mats[i], alpha, ro, tmax)[1]
                        delta = abs(ans_length - length)
                        min_d =  delta if min_d == -1 or min_d > delta else min_d
                        max_d =  delta if max_d == -1 or max_d < delta else max_d
                        sum_d += delta
                    mean_d = sum_d / MAX_ITERS
                    str += f" & {min_d} & {max_d} & {mean_d}"
                str += " \\\\ "
                print(str)

if __name__ == '__main__':
    generate()