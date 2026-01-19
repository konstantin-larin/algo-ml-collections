---
tags:
  - problem
level: easy
---

Дата: [[19-06-2025]]

# Ссылка: 
https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

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

    def removeElement(self, nums, val):

        """

        :type nums: List[int]

        :type val: int

        :rtype: int

        """

        k = 0

        for i in range(len(nums)):

            if nums[i] != val:

                nums[k] = nums[i]

                k += 1

        return k
```
# Ревью
было довольно легко после [[Triangle]] 
