from collections import deque


def bfs_shortest_path(graph, start):
    # Словарь для хранения кратчайших путей
    shortest_paths = {start: [start]}
    # Очередь для BFS
    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        # Проходим по всем соседям текущей вершины
        for neighbor in graph[current_node]:
            # Если сосед еще не посещен
            if neighbor not in shortest_paths:
                # Записываем кратчайший путь до соседа
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]
                # Добавляем соседа в очередь
                queue.append(neighbor)

    return shortest_paths


def input_graph():
    graph = {}
    print("Введите граф в формате 'вершина: сосед1, сосед2, ...'. Введите 'стоп' для завершения ввода.")

    while True:
        line = input("Введите вершину и её соседей: ")
        if line.lower() == 'стоп':
            break
        try:
            node, neighbors = line.split(':')
            node = node.strip()
            neighbors = [n.strip() for n in neighbors.split(',')]
            graph[node] = neighbors
        except ValueError:
            print("Неверный формат. Пожалуйста, используйте формат 'вершина: сосед1, сосед2, ...'.")

    return graph


if __name__ == "__main__":
    # Ввод графа пользователем
    graph = input_graph()

    # Ввод начальной вершины
    start_node = input("Введите начальную вершину: ").strip()

    # Проверка, существует ли начальная вершина в графе
    if start_node not in graph:
        print(f"Вершина '{start_node}' не найдена в графе.")
    else:
        # Получение кратчайших путей
        shortest_paths = bfs_shortest_path(graph, start_node)

        # Выводим кратчайшие пути от начальной вершины
        for node, path in shortest_paths.items():
            print(f"Кратчайший путь от {start_node} до {node}: {path}")




