def standard_mult(mat_a, mat_b):
    if len(mat_a) == 0 or len(mat_b) == 0:
        return []
    na = len(mat_a)
    ma = len(mat_a[0])
    nb = len(mat_b)
    mb = len(mat_b[0])
    if ma != nb:
        return []

    mat_c = [[0] * mb for i in range(na)]
    for i in range(na):
        for j in range(mb):
            for k in range(ma):
                mat_c[i][j] = mat_c[i][j] + mat_a[i][k] * mat_b[k][j]

    return mat_c


def vinograd_alg(mat_a, mat_b):
    if len(mat_a) == 0 or len(mat_b) == 0:
        return []
    na = len(mat_a)
    ma = len(mat_a[0])
    nb = len(mat_b)
    mb = len(mat_b[0])
    if ma != nb:
        return []

    mat_c = [[0] * mb for i in range(na)]

    mul_h = [0] * na
    for i in range(na):
        for j in range(ma // 2):
            mul_h[i] = mul_h[i] + mat_a[i][2 * j] * mat_a[i][2 * j + 1]

    mul_v = [0] * mb
    for j in range(mb):
        for k in range(nb // 2):
            mul_v[j] = mul_v[j] + mat_b[2 * k][j] * mat_b[2 * k + 1][j]

    for i in range(na):
        for j in range(mb):
            mat_c[i][j] = -mul_h[i] - mul_v[j]
            for k in range(ma // 2):
                mat_c[i][j] = mat_c[i][j] + (mat_a[i][2 * k] + mat_b[2 * k + 1][j]) * \
                              (mat_a[i][2 * k + 1] + mat_b[2 * k][j])

    if ma % 2 == 1:
        for i in range(na):
            for j in range(mb):
                mat_c[i][j] = mat_c[i][j] + mat_a[i][ma - 1] * mat_b[nb - 1][j]

    return mat_c


def optimized_vinograd_alg(mat_a, mat_b):
    if len(mat_a) == 0 or len(mat_b) == 0:
        return []
    na = len(mat_a)
    ma = len(mat_a[0])
    nb = len(mat_b)
    mb = len(mat_b[0])
    if ma != nb:
        return []

    mat_c = [[0] * mb for i in range(na)]

    mul_h = [0] * na
    for i in range(na):
        for j in range(1, ma, 2):
            mul_h[i] += mat_a[i][j] * mat_a[i][j - 1]

    mul_v = [0] * mb
    for j in range(mb):
        for k in range(1, nb, 2):
            mul_v[j] += mat_b[k][j] * mat_b[k - 1][j]

    if ma > 1:
        for i in range(na):
            for j in range(mb):
                mat_c[i][j] = (mat_a[i][0] + mat_b[1][j]) * (mat_a[i][1] + mat_b[0][j]) - \
                               mul_h[i] - mul_v[j]
                for k in range(2, ma - 1, 2):
                    mat_c[i][j] += (mat_a[i][k] + mat_b[k + 1][j]) * \
                                  (mat_a[i][k + 1] + mat_b[k][j])

    if ma % 2 == 1:
        for i in range(na):
            for j in range(mb):
                mat_c[i][j] += mat_a[i][ma - 1] * mat_b[nb - 1][j]

    return mat_c
