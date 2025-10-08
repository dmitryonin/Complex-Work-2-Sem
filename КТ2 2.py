class Graph:
    def __init__(self, n: int):
        self.n = n
        self.INF = float('inf')
        self.matrix = [[0] * n for _ in range(n)]

    def set_matrix(self, matrix):
        if len(matrix) != self.n or any(len(row) != self.n for row in matrix):
            raise ValueError("Матрица должна быть размером N×N.")
        self.matrix = matrix

    def shortest_way(self):
        n = self.n
        dist = [row[:] for row in self.matrix]
        #алгоритм флойда уоршелла

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

    def has_negative_cycle(self, dist, start, end):
        for v in range(self.n):
            if dist[v][v] < 0 and dist[start][v] < self.INF and dist[v][end] < self.INF:
                return True
        return False

    def shortest_path(self, start: int, end: int):
        dist = self.shortest_way()
        start -= 1
        end -= 1

        if self.has_negative_cycle(dist, start, end):
            return None
        return dist[start][end]




K = int(input("Введите номер начальной вершины K: "))
M = int(input("Введите номер конечной вершины M: "))
N = int(input("Введите количество вершин N (1 ≤ N ≤ 100): "))

print("\nВведите матрицу смежности графа (N строк по N чисел):")
print("На главной диагонали всегда нули.")

matrix = []
for i in range(N):
    row = list(map(int, input(f"Строка {i+1}: ").split()))
    if len(row) != N:
        raise ValueError(f"Ошибка: в строке {i+1} должно быть {N} чисел.")
    matrix.append(row)

graph = Graph(N)
graph.set_matrix(matrix)

result = graph.shortest_path(K, M)

if result is None:
    print("\nПуть имеет отрицательный цикл. Его длина может быть сколь угодно малой (-INF).")
else:
    print(f"\nДлина кратчайшего пути из вершины {K} в вершину {M}: {result}")


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
