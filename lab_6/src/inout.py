from random import randint

def input_mat():
    n = int(input("Введите количество вершин в графе: "))
    print("Введите матрицу расстояний")
    mat = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(float(input(f'Введите {j + 1}-ое значение {i + 1}-ой строки: ')))
        mat.append(row)
    print("Полученная матрица расстояний:")
    output_mat(n, mat)
    return mat

def random_mat(n):
    mat = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(randint(1, 20) if i != j else 0)
        mat.append(row)
    return mat

def output_mat(n, mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j], end=' ')
        print()

def input_coefs():
    alpha = float(input("Введите коэффициент alpha: "))
    ro = float(input("Введите коэффициент ro: "))
    t_max = int(input("Введите коэффициент t_max: "))
    return alpha, ro, t_max

def input_mat_from_file(filename):
    file = open(filename, "r")
    data = file.readlines()
    mat = list()
    for row in data:
        mat.append(row[:-1].split())
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = int(mat[i][j])
    return mat
