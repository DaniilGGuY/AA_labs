from itertools import permutations

def standard_alg(mat):
    n = len(mat)
    vertexes = [ i + 1 for i in range(n) ]
    min_path_len = -1
    best_path = tuple()
    for path in permutations(vertexes):
        path_len = 0
        for i in range(len(path) - 1):
            a, b = path[i], path[i + 1]
            path_len += mat[a - 1][b - 1]
        if min_path_len == -1 or min_path_len > path_len:
            min_path_len = path_len
            best_path = path
    return list(best_path), min_path_len

