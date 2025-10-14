class Graph:
    def __init__(self, n: int):
        self.n = n
        self.INF = 10 ** 9
        self.matrix = [[0 if i == j else self.INF for j in range(n)] for i in range(n)]

    def set_matrix(self, matrix):
        for i, row in enumerate(matrix):
            if row[i] != 0:
                raise ValueError(f"Диагональный элемент matrix[{i}][{i}] должен быть 0")
        self.matrix = [row[:] for row in matrix]

    def floyd_warshall(self):
        dist = [row[:] for row in self.matrix]
        for k in range(self.n):
            for i in range(self.n):
                if dist[i][k] == self.INF:
                    continue
                for j in range(self.n):
                    new_distance = dist[i][k] + dist[k][j]
                    if new_distance < dist[i][j]:
                        dist[i][j] = new_distance
        return dist

    def has_negative_cycle_on_path(self, dist, start, end):
        for v in range(self.n):
            if dist[v][v] < 0 and dist[start][v] < self.INF and dist[v][end] < self.INF:
                return True
        return False

    def shortest_path(self, start: int, end: int):
        start_idx = start - 1
        end_idx = end - 1
        dist = self.floyd_warshall()
        if self.has_negative_cycle_on_path(dist, start_idx, end_idx):
            return None
        return dist[start_idx][end_idx] if dist[start_idx][end_idx] < self.INF else self.INF

    def __str__(self):
        return f"Graph(n={self.n})"

    def print_matrix(self):
        print("Матрица смежности:")
        for row in self.matrix:
            print(" ".join(f"{x:8}" if x != self.INF else "     INF" for x in row))


def input_and_validate_data():
    while True:
        try:
            N = int(input("Введите количество вершин N (1 ≤ N ≤ 100): "))
            if 1 <= N <= 100:
                break
            print("Ошибка: N должно быть от 1 до 100")
        except ValueError:
            print("Ошибка: введите целое число")

    while True:
        try:
            K = int(input("Введите номер начальной вершины K: "))
            if 1 <= K <= N:
                break
            print(f"Ошибка: K должно быть от 1 до {N}")
        except ValueError:
            print("Ошибка: введите целое число")

    while True:
        try:
            M = int(input("Введите номер конечной вершины M: "))
            if 1 <= M <= N:
                break
            print(f"Ошибка: M должно быть от 1 до {N}")
        except ValueError:
            print("Ошибка: введите целое число")

    print(f"\nВведите матрицу смежности графа {N}×{N}:")

    matrix = []
    for i in range(N):
        while True:
            try:
                row_input = input(f"Строка {i + 1}: ").split()
                if len(row_input) != N:
                    print(f"Ошибка: введите ровно {N} чисел")
                    continue

                row = []
                for j, num_str in enumerate(row_input):
                    if num_str.upper() == "INF":
                        value = 10 ** 9
                    else:
                        value = int(num_str)

                    if i == j and value != 0:
                        print(f"Предупреждение: диагональный элемент matrix[{i}][{j}] установлен в 0")
                        value = 0

                    row.append(value)

                matrix.append(row)
                break

            except ValueError:
                print("Ошибка: введите целые числа или INF")

    return N, K, M, matrix


N, K, M, matrix = input_and_validate_data()

graph = Graph(N)
graph.set_matrix(matrix)

print("\n" + "=" * 50)
result = graph.shortest_path(K, M)

if result is None:
    print(f"Путь из вершины {K} в вершину {M} имеет отрицательный цикл.")
    print("Длина пути может быть сколь угодно малой (-INF).")
elif result == graph.INF:
    print(f"Путь из вершины {K} в вершину {M} не существует.")
else:
    print(f"Длина кратчайшего пути из вершины {K} в вершину {M}: {result}")

'''
 K: 1
 M: 3
 N: 3

Строка 1: 0 2 5
Строка 2: 2 0 1
Строка 3: 5 1 0

K = 1
M = 3
N = 3

Строка 1: 0 -2 4
Строка 2: 1 0 3
Строка 3: 2 -1 0

K = 1
M = 4
N = 4

Строка 1: 0 1 10 100
Строка 2: 1 0 1 100
Строка 3: 10 1 0 1
Строка 4: 100 100 1 0

K = 1
M = 3
N = 3

Строка 1: 0 1 10
Строка 2: -2 0 3
Строка 3: 4 -5 0

K = 2
M = 3
N = 3

Строка 1: 0 5 1
Строка 2: 2 0 2
Строка 3: 5 1 0

'''
