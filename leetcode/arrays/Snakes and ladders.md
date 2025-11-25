---
tags:
  - problem
level: medium
---
Дата: 2025-06-10

# Ссылка: 
https://leetcode.com/problems/snakes-and-ladders/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

![[Snakes and ladders 2025-06-10 10.12.08.excalidraw]]
# Код
```python
from collections import deque

class Solution(object):

    def snakesAndLadders(self, board):

        """

        :type board: List[List[int]]

        :rtype: int

        """

        # 1 - преобразуем доску в одномерный массив

        n = len(board)

        end = n ** 2

        reversed_board = board[::-1]        

        arr = []

        for i in range(n):

            row = reversed_board[i]

            if i % 2 == 0:

                # строка идет слева направо

                arr.extend(row)

            else:

                arr.extend(row[::-1])

        # bfs

        queue = deque([0])

        visited = set([0])

        steps_count = 0

        while queue:

            level_size = len(queue)

            steps_count += 1

            print(queue)

            for _ in range(level_size):                

                idx = queue.popleft()                

                for i in range(idx + 1, min(end, idx + 7)):

                    print(i)

                    el = arr[i]

                    v = i                                

                    if el != -1:

                        v = el - 1

                    if v not in visited:

                        queue.append(v)

                        visited.add(v)

                    if v == end - 1:
                        return steps_count

        return -1
```
# Ревью
Вот тут немного другая реализация bfs.
```python
class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        min_rolls = [-1] * (n * n + 1)
        q = deque()
        min_rolls[1] = 0
        q.append(1)

        while q:
            x = q.popleft()
            for i in range(1, 7):
                t = x + i
                if t > n * n:
                    break
                row = (t - 1) // n
                col = (t - 1) % n
                v = board[n - 1 - row][(n - 1 - col) if (row % 2 == 1) else col]
                y = v if v > 0 else t
                if y == n * n:
                    return min_rolls[x] + 1
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y)
        return -1
```