

import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання станцій (вершин)
stations = ['Station1', 'Station2', 'Station3', 'Station4', 'Station5']

# Додавання маршрутів (ребер) з вагами (час в хвилинах)
edges = [
    ('Station1', 'Station2', 5),
    ('Station1', 'Station3', 10),
    ('Station2', 'Station3', 3),
    ('Station2', 'Station4', 8),
    ('Station3', 'Station4', 2),
    ('Station4', 'Station5', 7),
    ('Station3', 'Station5', 4)
]

# Додавання ребер до графа
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Transport Network")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degrees = dict(G.degree())
average_degree = sum(degrees.values()) / num_nodes

print(f'Кількість вершин: {num_nodes}')
print(f'Кількість ребер: {num_edges}')
print(f'Ступені вершин: {degrees}')
print(f'Середній ступінь: {average_degree:.2f}')
