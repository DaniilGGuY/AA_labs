from algs import standard_mult, vinograd_alg, optimized_vinograd_alg
from tests import testing
from input_output import input_mat, output_mat
from research import research

while True:
    print("Меню:")
    print("1 - Тестирование программы")
    print("2 - Ручной ввод матриц")
    print("3 - Провести исследование алгоритмов")
    print("0 - Завершить программу")
    action = int(input("Введите номер команды: "))
    if action == 0:
        break
    elif action == 1:
        testing()
    elif action == 2:
        print("\nINPUT FIRST MATRIX")
        mat_a = input_mat()
        print("\nINPUT SECOND MATRIX")
        mat_b = input_mat()
        ans_1 = standard_mult(mat_a, mat_b)
        ans_2 = vinograd_alg(mat_a, mat_b)
        ans_3 = optimized_vinograd_alg(mat_a, mat_b)
        if len(ans_1) != 0:
            print("\nSTANDARD ALGORITHM ANSWER:")
            output_mat(ans_1)
            print("\nVINOGRAD ALGORITHM ANSWER:")
            output_mat(ans_2)
            print("\nOPTIMIZED VINOGRAD ALGORITHM ANSWER:")
            output_mat(ans_3)
        else:
            print("\nNO ANSWER. INCORRECT SIZES OF MATRIXES\n")
    elif action == 3:
        research()  
