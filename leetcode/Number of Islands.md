---
tags:
  - problem
level: medium
---

Дата: 2025-06-09

# Ссылка: 
https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

[[Number of Islands 2025-06-09 18.21.56.excalidraw]]
Идея: пройтись по всем элементам. Для каждого элемента проверять элемент слева и сверху. 
Так как мы будем идти слева направо и сверху вниз, будет гарантировано, что если возле единицы есть другая единичка, то она уже в islands. Проверяем по координатам (мы записываем координаты в islands) в каком наборе лежит единица-сосед. Кладем текущую единицу туда же. При этом ясно, что если мы натыкаемся на единицу, у которой слева и сверху нет соседа - это новый остров.

идея почти зашла но \[\["1","1","1"],\["0","1","0"],\["1","1","1"]] вот этот тест показал, что нужно проверять и справа единицу и снизу, но не факт конечно, что они окажутся на острове (скорее всего нет), но такие случаи есть и их надо проверять.
вот код идея не сработала на том же тесте, появилась другая сейчас.
```python
class Solution(object):

    def numIslands(self, grid):

        """

        :type grid: List[List[str]]

        :rtype: int

        """        

        m = len(grid)

        n = len(grid[0])

        islands = []  

        def post_to_islands(cur_coords, ne_coords):            

            is_posted = False

            for isl in islands:

                if ne_coords in isl:

                    is_posted = True

                    isl.add(cur_coords)                    

                    break          

            return is_posted

  

        for i in range(m):

            for j in range(n):

                if grid[i][j] == '1':

                    i_top = i - 1

                    i_bottom = i + 1

                    j_left = j - 1

                    j_right = j + 1

                    if j_left >= 0 and grid[i][j_left] == '1':

                        if post_to_islands( (i, j) , (i, j_left) ):

                            continue

                    if i_top >= 0 and grid[i_top][j] == '1':

                        if post_to_islands( (i, j) , (i_top, j) ):

                            continue

                    if i_bottom < m and grid[i_bottom][j] == '1':

                        if post_to_islands( (i, j) , (i_bottom, j) ):

                            continue

                    if j_right < n and grid[i][j_right] == '1':

                        if post_to_islands( (i, j) , (i, j_right) ):

                            continue

                    # соседей нет, образуем новый остров

                    islands.append(set([(i, j)]))

        print(islands)

        return len(islands)
```

идея 2: обход в глубину как с деревом - проходим ячейки, натыкаемся на первую попавшуюся единицу и если она не посещена была уже попадаем в цикл. И дальше bfs как с графом - ищем соседей связанных, добавляем их в очередь, продолжаем цикл пока очередь не кончится считаем counter количество островов. По сути острова в данном виде можно представить как несвязный граф.
# Код
```python
from collections import deque

class Solution(object):

    def numIslands(self, grid):

        """

        :type grid: List[List[str]]

        :rtype: int

        """        

        m = len(grid)

        n = len(grid[0])

        islands_counter = 0

        visited_parts = set()

        for i in range(m):

            for j in range(n):

                if grid[i][j] == '1' and (i, j) not in visited_parts:

                    islands_counter += 1

                    queue = deque([(i, j)])

                    while queue:                        

                        h, v = queue.popleft()                                                

  

                        if h  > 0 and grid[h - 1][v] == '1' and (h-1, v) not in visited_parts:

                            visited_parts.add( (h-1, v) )

                            queue.append( (h-1, v) )

  

                        if h + 1 < m and grid[h + 1][v] == '1' and (h+1, v) not in visited_parts:

                            visited_parts.add( (h+1, v) )                            

                            queue.append( (h+1, v) )

  

                        if v  > 0 and grid[h][v - 1] == '1' and (h, v - 1) not in visited_parts:                            

                            visited_parts.add( (h, v - 1) )

                            queue.append( (h, v - 1) )

  

                        if v + 1 < n and grid[h][v + 1] == '1' and (h, v + 1) not in visited_parts:

                            visited_parts.add( (h, v + 1) )                                                        

                            queue.append( (h, v + 1) )          

  
  

        return islands_counter
```
# Ревью

Решил правильно, кардинально другой идеи нет.
```python

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1" and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands

```