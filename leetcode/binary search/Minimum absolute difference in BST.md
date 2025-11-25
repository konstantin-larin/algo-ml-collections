---
tags:
  - problem
level: easy
---
Дата: 2025-06-09

# Ссылка: 
[Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/)

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код
Найти минимальную абсолютную разницу между **любыми** элементами дерева.
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Код, который не прошел все тесты
```python
# Definition for a binary tree node. 
# class TreeNode(object): # def __init__(self, val=0, left=None, right=None): # self.val = val # self.left = left # self.right = right 
class Solution(object): 
	def getMinimumDifference(self, root): 
		""" :type root: Optional[TreeNode] :rtype: int """ 
		left = root.left 
		left_diff = float('inf') 
		if left: 
			left_diff = min(root.val - left.val, self.getMinimumDifference(left)) 
			
		right = root.right 
		right_diff = float('inf')\ 
		if right: 
			right_diff = min(right.val - root.val, self.getMinimumDifference(right)) 
			
		return min(right_diff, left_diff)
```
Тут ошибка в том, что я просматриваю только соседей, но сказано, что 2 узла могут быть где угодно
У каких элементов разница будет точно не минимальной? Ясно, что если возьмем любой элемент дерева, то его левый элемент будет меньше его, правый - больше. Соответственно любой элемент, который будет находиться от данного по одну сторону (то есть доступ к нему будет таким: node.left.left... или node.right.right....), не может составлять минимальную разницу с данным элементом. Соответственно надо искать какие-то комбинации right-left left-right... 
Конечно можно решить эту задачу брутом за O(n^2), но ясно, что с бинарным деревом надо поступать умнее. 
Немного посмотрев дискуссии, увидел следующее:

A binary search tree has the property that the sequence obtained through an in-order traversal is a sorted array.

Therefore, we only need to perform an in-order traversal and calculate the absolute difference between each pair of adjacent numbers. The minimum difference obtained will be the desired result.v



```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binary_tree_traversal(self, node, prev_node_val, result):
        if node is None:
            return
        self.binary_tree_traversal(node.left, node.val, result)
        result.append(abs(node.val - prev_node_val))                
        self.binary_tree_traversal(node.right, node.val, result) 
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = []
        self.binary_tree_traversal(root, float('inf'), result)
        print(result)
        return min(result)

        
```     

немного неверная реализация, надо сначала все вершины сложить в порядке возрастания а затем отдельным перебором все посчитать.

# Код 
```python
# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution(object):

    def binary_tree_traversal(self, node, result):

        if node is None:

            return

        self.binary_tree_traversal(node.left, result)

        result.append(node.val)                

        self.binary_tree_traversal(node.right, result)

    def getMinimumDifference(self, root):

        """

        :type root: Optional[TreeNode]

        :rtype: int

        """

        result = []

        self.binary_tree_traversal(root, result)

        min_diff = float('inf')

        for i in range(len(result) - 1):

            min_diff = min(result[i + 1] - result[i], min_diff)

        return min_diff
```

# Ревью

Нашел другое решение оно также с bst.

![[Minimum absolute difference in BST 2025-06-09 17.38.11.excalidraw]]



```python
# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

class Solution(object):

    def binary_tree_traversal(self, node):

        if node:

            self.binary_tree_traversal(node.left)

            if self.prev is not None:

                self.min_diff = min(self.min_diff, node.val - self.prev)

            self.prev = node.val

            self.binary_tree_traversal(node.right)

    def getMinimumDifference(self, root):

        """

        :type root: Optional[TreeNode]

        :rtype: int

        """

        self.prev = None

        self.min_diff = float('inf')        

        self.binary_tree_traversal(root)        

        return self.min_diff
```