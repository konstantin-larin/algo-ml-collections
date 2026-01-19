---
date: "05-05-2025"
tags:
  - problem
level: easy
---
```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-05-05T20:27:35.246Z","endTime":"2025-05-05T20:50:31.478Z"},{"name":"Segment 2","startTime":"2025-05-12T09:03:11.680Z","endTime":"2025-05-12T09:38:37.142Z"}]}
```


# Задача:

Ссылка: https://leetcode.com/problems/two-sum/description/?envType=problem-list-v2&envId=array

Что нужно?

Вход:
1: Массив уникальных чисел 
2: target - сумма из двух каких-то чисел из массива

Выход:
индексы этих двух чисел в любом порядке
# Теория/рассуждения
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем.

O(n2) ясно.
Но как решить лучше?

Подожди! так это же [[Рюкзак наибольшая стоимость]].

![[two sum 2025-05-12 12.24.31.excalidraw]]

# Code
```python
class Solution(object):  
    def twoSum(self, nums, target):  
        """  

        :type nums: List[int]        :type target: int        :rtype: List[int]  

        """                        

        hash_table = dict()

        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]

            hash_table[num] = i
```

# Review

Идея о том, что надо просто искать число target - num уменьшает сложность с O(n^2) до O(n) хороша. 
