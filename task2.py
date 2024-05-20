
from task1 import G
from collections import deque


# Реалізація алгоритму DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Реалізація алгоритму BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Визначення початкової та кінцевої станції
start_station = 'Station1'
goal_station = 'Station5'

# Знаходження шляхів за допомогою DFS
dfs_paths = list(dfs(G, start_station, goal_station))
print(f'Шляхи від {start_station} до {goal_station} за допомогою DFS:')
for path in dfs_paths:
    print(path)

# Знаходження шляхів за допомогою BFS
bfs_paths = list(bfs(G, start_station, goal_station))
print(f'Шляхи від {start_station} до {goal_station} за допомогою BFS:')
for path in bfs_paths:
    print(path)

# Порівняння результатів
print(f'Різниця між DFS та BFS:')
print(f'Кількість шляхів за допомогою DFS: {len(dfs_paths)}')
print(f'Кількість шляхів за допомогою BFS: {len(bfs_paths)}')