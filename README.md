goit-algo-hw-06

## Висновок до task2.py
### DFS (Depth-First Search)
Алгоритм DFS виконує глибокий пошук, тобто спочатку досліджує якомога глибше по кожному шляху, перш ніж повернутися назад. В результаті він знаходить шляхи від Station1 до Station5 наступним чином:

```python
Шляхи від Station1 до Station5 за допомогою DFS:

['Station1', 'Station3', 'Station5']
['Station1', 'Station2', 'Station4', 'Station5']
```
DFS може знайти декілька шляхів, але не гарантує, що знайдений шлях буде найкоротшим.

### BFS (Breadth-First Search)
Алгоритм BFS виконує пошук у ширину, тобто досліджує всі вершини на поточному рівні перед переходом на наступний рівень. Це гарантує, що знайдений шлях буде найкоротшим у незваженому графі. В результаті він знаходить шляхи від Station1 до Station5 наступним чином:

```python
Шляхи від Station1 до Station5 за допомогою BFS:
['Station1', 'Station3', 'Station5']
['Station1', 'Station2', 'Station4', 'Station5']
```
BFS також може знайти декілька шляхів, але всі знайдені шляхи будуть найкоротшими у термінах кількості ребер.

### Висновки
Шляхи, знайдені обома алгоритмами, можуть бути однаковими, але спосіб їхнього знаходження відрізняється.
DFS знаходить шляхи шляхом глибокого пошуку, що не гарантує найкоротший шлях. В нашому прикладі він знайшов два шляхи.

BFS знаходить найкоротший шлях у термінах кількості ребер, тому він завжди гарантує знайдення оптимального шляху. В нашому прикладі він також знайшов два шляхи, але вони були найкоротшими.

В обох випадках обидва алгоритми знайшли ті ж самі шляхи, оскільки у графі були чітко визначені шляхи з однаковою кількістю ребер.

Таким чином, вибір алгоритму залежить від конкретного завдання. Якщо потрібно знайти найкоротший шлях в незваженому графі, краще використовувати BFS. Якщо ж важливе повне дослідження всіх можливих шляхів, можна використовувати DFS.