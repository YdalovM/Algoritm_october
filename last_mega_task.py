n, m, q = map(int, input().split())             # Вводим кол-во сезонов, серий в сезонеб серий на платформе5,1,2
x = [[0] * n for i in [0] * m]                  # Создаем список списков
for i in range(q):                              # Цикл, который будет выполнен q раз
    i, j = map(int, input().split())            # Вписываем номер сзона и номер эпизода
    x[i - 1][j - 1] = 1                         # Хаменяем их в списке на значение 1
print(m * n - sum(sum(x, [])))                  # Вывод номер эпизода и номер сезона
for i in range(n):                              # Цикл, который будет выполнен n раз.
    for j in range(m):                          # Цикл, который будет выполнен m раз
        if x[j][i] != 1: print(j + 1, i + 1)    # Если в списке есть значения эпизода и серий не равно 1 выводит их координаты


                                                # Misha 💔