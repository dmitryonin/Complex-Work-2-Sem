from collections import deque

print("\nВведите данные о графе:")
print("Сначала введите два числа: количество вершин и начальную вершину")
print("Затем введите матрицу смежности построчно")

try:
    data = input("Введите N и S: ").split()
    if len(data) != 2:
        print("Ошибка: нужно ввести ровно два числа!")
        exit()

    n = int(data[0])
    s = int(data[1])

    if n < 1 or n > 100:
        print("Ошибка: N должно быть в диапазоне от 1 до 100!")
        exit()

    if s < 1 or s > n:
        print(f"Ошибка: S должно быть в диапазоне от 1 до {n}!")
        exit()

    print(f"\nВведите матрицу смежности {n}x{n}:")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Строка {i + 1}: ").split()))
        if len(row) != n:
            print(f"Ошибка: в строке должно быть ровно {n} чисел!")
            exit()
        graph.append(row)

    for i in range(n):
        for j in range(n):
            if graph[i][j] not in [0, 1]:
                print("Ошибка: матрица должна содержать только 0 и 1!")
                exit()
            if i == j and graph[i][j] != 0:
                print("Ошибка: на главной диагонали должны быть нули!")
                exit()
            if graph[i][j] != graph[j][i]:
                print("Ошибка: матрица должна быть симметричной!")
                exit()

    visited = [False] * n
    component = []

    start = s - 1
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()
        component.append(vertex + 1)

        for neighbor in range(n):
            if graph[vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    component.sort()

    print("РЕЗУЛЬТАТЫ:")
    print(f"Количество вершин в компоненте связности с вершиной {s}: {len(component)}")
    print(f"Вершины в компоненте связности: {' '.join(map(str, component))}")

except ValueError:
    print("Ошибка: введите корректные числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")