from random import random

def ant_alg(mat, alpha, ro, t_max):
    n, q = len(mat), calc_q(mat)
    pheromone = init_pheromone(n)
    attract = init_attract(mat)
    min_path_len = -1
    best_path = list()
    for t in range(t_max):
        memory = init_memory(n)
        for ant in range(n):
            while len(memory[ant]) != n:
                p = calc_p(pheromone, attract, memory[ant], n, alpha)
                memory[ant].append(calc_next(p))
            path_len = calc_length(mat, memory[ant])
            if min_path_len == -1 or min_path_len > path_len:
                min_path_len = path_len
                best_path = memory[ant]
        pheromone = update_pheromone(mat, memory, pheromone, q, ro)
    for i in range(len(best_path)):
        best_path[i] += 1
    return best_path, min_path_len

def calc_q(mat):
    n, q = len(mat), 0
    for i in range(n):
        for j in range(n):
            if i != j:
                q += mat[i][j]
    return q / (n ** 3 - n)

def init_pheromone(n):
    return [[1 for i in range(n)] for j in range(n)]

def init_attract(mat):
    return [[(1 / mat[i][j] if i != j else 0) for i in range(len(mat))] for j in range(len(mat))]

def init_memory(n):
    memory = list()
    for i in range(n):
        memory.append([i])
    return memory

def calc_p(pheromon, attract, memory, n, alpha):
    beta = 1 - alpha
    p = [0] * n
    for new_pos in range(n):
        if new_pos in memory:
            p[new_pos] = 0
        else:
            last_pos = memory[-1]
            p[new_pos] = pheromon[last_pos][new_pos] ** beta * attract[last_pos][new_pos] ** alpha
    psum = sum(p)
    for i in range(n):
        p[i] /= psum
    return p

def calc_next(p):
    point = random()
    i = 0
    while i < len(p):
        if point - p[i] < 0:
            return i
        point -= p[i]
        i += 1
    return len(p)

def calc_length(mat, path):
    length = 0
    for i in range(len(path) - 1):
        a, b = path[i], path[i + 1]
        length += mat[a][b]
    return length

def update_pheromone(mat, memory, pheromone, q, ro):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            delta = 0
            for ant in range(n):
                length = calc_length(mat, memory[ant])
                delta += q / length
            pheromone[i][j] = pheromone[i][j] * (1 - ro) + delta
            if pheromone[i][j] < 0.01:
                pheromone[i][j] = 0.01
    return pheromone
