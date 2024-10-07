def input_mat():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    mat = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j] = float(input(f'Введите {j + 1}-ый элемент {i + 1}-ой строки: '))
    return mat


def output_mat(mat):
    print(f'Количество строк: {len(mat)}, количество столбцов: {len(mat[0])}')
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=' ')
        print()
    print()