def recursive_alg(s1, s2):
    if len(s1) == 0:
        return len(s2)
    elif len(s2) == 0:
        return len(s1)
    elif s1[0] == s2[0]:
        return recursive_alg(s1[1:], s2[1:])

    return 1 + min(recursive_alg(s1[1:], s2),
                   recursive_alg(s1, s2[1:]),
                   recursive_alg(s1[1:], s2[1:]))


def DP_alg(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(m + 1):
        matrix[0][i] = i

    for i in range(n + 1):
        matrix[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            el = min(matrix[i - 1][j],
                     matrix[i - 1][j - 1],
                     matrix[i][j - 1])
            if s1[i - 1] != s2[j - 1]:
                el += 1
            matrix[i][j] = el

    return matrix[-1][-1]


def cache_alg(s1, s2, cache_mat):
    ind_i = len(cache_mat) - len(s1) - 1
    ind_j = len(cache_mat[0]) - len(s2) - 1
    if len(s1) == 0:
        cache_mat[ind_i][ind_j] = len(s2)
        return len(s2)
    elif len(s2) == 0:
        cache_mat[ind_i][ind_j] = len(s1)
        return len(s1)
    elif s1[0] == s2[0]:
        el = cache_mat[ind_i + 1][ind_j + 1]
        return el if el != -1 else cache_alg(s1[1:], s2[1:], cache_mat)

    el_1 = cache_mat[ind_i + 1][ind_j]
    el_2 = cache_mat[ind_i][ind_j + 1]
    el_3 = cache_mat[ind_i + 1][ind_j + 1]
    return 1 + min(el_1 if el_1 != -1 else cache_alg(s1[1:], s2, cache_mat),
                   el_2 if el_2 != -1 else cache_alg(s1, s2[1:], cache_mat),
                   el_3 if el_3 != -1 else cache_alg(s1[1:], s2[1:], cache_mat))


def damerau_alg(s1, s2):
    n = len(s1)
    m = len(s2)
    matrix = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(m + 1):
        matrix[0][i] = i

    for i in range(n + 1):
        matrix[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            el = min(matrix[i - 1][j],
                     matrix[i - 1][j - 1],
                     matrix[i][j - 1])
            if s1[i - 1] != s2[j - 1]:
                el += 1
            if i > 1 and j > 1 and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j  - 1]:
                el = min(el, matrix[i - 2][j - 2] + 1)
            matrix[i][j] = el

    return matrix[-1][-1]
