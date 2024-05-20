

from task1 import G
from task1 import stations

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, attributes in graph[current_vertex].items():
            distance = distances[current_vertex] + attributes['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)

    return distances

# Знаходження найкоротших шляхів від кожної вершини до всіх інших
for station in stations:
    shortest_paths = dijkstra(G, station)
    print(f'Найкоротші шляхи від {station}: {shortest_paths}')