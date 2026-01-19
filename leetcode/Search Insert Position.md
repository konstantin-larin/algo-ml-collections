---
tags:
  - problem
level: easy
---

Дата: [[15-06-2025]]

# Ссылка: 
https://leetcode.com/problems/search-insert-position/submissions/1665060558/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Разделяй и властвуй
![[Search Insert Position 2025-06-15 18.12.43.excalidraw]]
# Код
```python
class Solution(object):

    def searchInsert(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: int

        """

        n = len(nums)

        def dfs(start, end):            

            if start < end:

                mid = (start + end) // 2                

                if nums[mid] == target:

                    return mid

                if nums[mid] > target:                                        

                    return dfs(start, mid - 1)

                if nums[mid] < target:

                    return dfs(mid + 1, end)                    

            else:

                if nums[start] >= target:

                    return start

                return start + 1

  

        return dfs(0, n - 1)
```
# Ревью

Решение без рекурсии

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
```
