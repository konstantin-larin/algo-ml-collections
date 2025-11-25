---
tags:
  - problem
level: medium
---

Дата: 2025-06-05
# Ссылка: 


# Понимание условия

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

можно по порядку проверить колонки и строки брутом, а потом сделать 9 шагов, проверив 3 на 3 поля....
По идее надо решить за O(9 x 9)
![[Valid Sudoku 2025-06-05 14.33.33.excalidraw]]
# Код
```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cells = [
            [
                set() for _ in range(3)
            ] for _ in range(3)            
        ]
        cols = [
            set() for _ in range(9)            
        ]

        for i in range(9):
            row = set()            
            for j in range(9):
                el = board[i][j]
                if el == '.':

                    continue

                if el in row:

                    return False                

                col = cols[j]

                if el in col:

                    return False                

                r_idx = i // 3

                c_idx = j // 3

                cell = cells[r_idx][c_idx]

                if el in cell:

                    return False

                row.add(el)

                col.add(el)

                cell.add(el)

        return True
```

# Ревью

Минусом своего решения я вижу использование памяти, т.е. я создаю транспонированную матрицу cols по сути, создаю еще двумерный массив с сетами (cells). А в целом решение бьет по времени 93% решений, 2мс всего, о чем я и сказал (решение не зависит от входных вообще)

Посмотрев другие решения, я понял, что решил довольно хорошо, оптимальным способом.
Вот возможная модификация с использованием defaultdict вместо массивов - немного улучшило память.

```python
from collections import defaultdict

  

class Solution(object):

    def isValidSudoku(self, board):

        """

        :type board: List[List[str]]

        :rtype: bool

        """            

        cols = defaultdict(set)

        cells = defaultdict(set)

  

        for i in range(9):

            row = set()            

            for j in range(9):

                el = board[i][j]

                if el == '.':

                    continue

                if el in row:

                    return False                                

                col = cols[j]

                if el in col:

                    return False                

                r_idx = i // 3

                c_idx = j // 3

                cell = cells[(r_idx, c_idx)]

                if el in cell:

                    return False

                row.add(el)

                col.add(el)

                cell.add(el)

        return True
```
