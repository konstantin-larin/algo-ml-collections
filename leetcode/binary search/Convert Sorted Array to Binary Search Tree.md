---
tags:
  - problem
level: easy
---

Дата: [[15-06-2025]]

# Ссылка: 
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
class Solution(object):

    def sortedArrayToBST(self, nums):

        """

        :type nums: List[int]

        :rtype: Optional[TreeNode]

        """

        n = len(nums)

        def convert_to_bst(start, end):

            if start > end:

                return None

            mid = (start + end) // 2

            root = TreeNode(

                val = nums[mid],

                left = convert_to_bst(start, mid - 1),

                right = convert_to_bst(mid + 1, end)

                )

            return root

        return convert_to_bst(0, n - 1)
```
# Ревью
Использовал подход "Разделяй и Властвуй".