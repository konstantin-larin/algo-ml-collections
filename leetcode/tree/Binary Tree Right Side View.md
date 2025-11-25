---
tags:
  - problem
level: medium
---

Дата: 2025-06-09

# Ссылка: 
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Буду использовать bfs.  Идея простая - при проходе bfs записывать правые элементы первыми в очередь (можно и последними - не важно). Тем самым становится понятно, нужно на проходе уровня записывать первый элемент, на который наткнемся - он и будет самым правым.
![[Binary Tree Right Side View 2025-06-09 10.20.37.excalidraw]]
# Код
```python
from collections import deque

# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution(object):

    def rightSideView(self, root):

        """

        :type root: Optional[TreeNode]

        :rtype: List[int]

        """

        if root is None:

            return []

        queue = deque([root])

        nums = []        

        while queue:            

            level_size = len(queue)  

            print(queue)          

            nums.append(queue[0].val)                

            for _ in range(level_size):

                node = queue.popleft()                

                if node.right:

                    queue.append(node.right)          

                if node.left:

                    queue.append(node.left)                

        return nums
```
# Ревью
Использовал bfs
