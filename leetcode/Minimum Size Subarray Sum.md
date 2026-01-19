---
tags:
  - problem
level: medium
---

Дата: 2025-06-02
```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-06-02T18:21:44.099Z","endTime":"2025-06-02T18:52:46.015Z"},{"name":"Segment 2","startTime":"2025-06-03T09:25:06.068Z","endTime":"2025-06-03T09:33:29.245Z"}]}
```
# Ссылка: 
https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150


# Понимание условия
Дан массив положительных чисел
Вернуть наименьшую длину массива, сумма элементов которого больше или равна target
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Используя концепцию скользящего окна попробовал так решить:
```python
class Solution(object):

    def minSubArrayLen(self, target, nums):

        """

        :type target: int

        :type nums: List[int]

        :rtype: int

        """

        ans = float('inf')

        l = 0

        r = 0

        n = len(nums)

        while l < n:

            subarr = nums[l:r]            

            if sum(subarr) >= target:

                ans = min(len(subarr), ans)

                l += 1

            elif r < n:

                r += 1

            else:

                break        

        return 0 if ans == float('inf') else ans
```

Но оказалось очень требовательно по времени.
Почему? Потому что операция sum() не бесплатна. Лучше считать сумму аккумулятивно,
# Код
```python
class Solution(object):

    def minSubArrayLen(self, target, nums):

        """

        :type target: int

        :type nums: List[int]

        :rtype: int

        """

        ans = float('inf')        

        l = 0

        r = 0

        n = len(nums)

        s = 0

        while l < n:            

            if s >= target:

                ans = min(r - l, ans)

                s -= nums[l]                

                l += 1

            elif r < n:                

                s += nums[r]

                r += 1

            else:                

                break

  

        return 0 if ans == float('inf') else ans
	
```
# Ревью
Вник в скользящее окно - мне нравится эта логика. 