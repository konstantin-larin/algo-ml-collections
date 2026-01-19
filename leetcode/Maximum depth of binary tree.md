---
tags:
  - problem
level: easy
---

Дата: 2025-06-05

# Ссылка: 
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150


# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер


Решу в dfs и bfs
# Код 

## DFS
```python
# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution(object):

    def maxDepth(self, root):

        """

        :type root: Optional[TreeNode]

        :rtype: int

        """                

        if root is None:

            return 0

        left_depth = self.maxDepth(root.left)

        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)	
```

## BFS
```python
from collections import deque

# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution(object):

    def maxDepth(self, root):

        """

        :type root: Optional[TreeNode]

        :rtype: int

        """                

        if root is None:

            return 0

        queue = deque([root])            

        depth = 0

        while queue:

            depth += 1

            level_size = len(queue)

            for i in range(level_size):

                node = queue.popleft()

                if node.left:

                    queue.append(node.left)

                if node.right:

                    queue.append(node.right)

        return depth
```
# Ревью
BFS более предпочтителен, так как работает без рекурсии, а на основе двусторонней очереди.