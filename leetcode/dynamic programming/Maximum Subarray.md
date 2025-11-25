---
tags:
  - problem
level: medium
---
Дата: [[15-06-2025]]

# Ссылка: 
https://leetcode.com/problems/maximum-subarray/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

**Дерево отрезков!**
![[Maximum Subarray 2025-06-15 16.06.18.excalidraw]]

Решение рабочее, но в случае, если нет отрицательных чисел, а у нас они есть
```python
import math

class Solution(object):

    def maxSubArray(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        # дерево отрезков

        n = len(nums)

        size = int(2 ** math.ceil(math.log(n, 2)) )

        print(size)

        neutral = 0

        arr = []

        for i in range(size):

            if i >= n:

                arr.append(neutral)

            else:

                arr.append(nums[i])

        arr = [neutral for _ in range(size - 1)] + arr

        print(arr)

        print(len(arr))

        for i in range(size - 2, -1, -1):        

            child_1 = arr[2 * i + 1]

            child_2 = arr[2 * i + 2]

            arr[i] = child_1 + child_2

        print(arr)

        return max(arr)
```

Идея: применить сравнение префиксного и постфиксного числа на отрезке, чтоб можно было складывать не просто числа, а выбирать наибольшие из них (так как допустим сумма префиксного и постфиксного может быть меньше чем префиксное число из-за отрицательных чисел )
# Код

```python

```
# Ревью
Не успел решить эту задачу. Ее в итоге можно решить тремя способами, но 
### Самый эффективный O(N) Алгоритм Кадана
```python
class Solution(object):    

    def maxSubArray(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        current_max = nums[0]    

        global_max = nums[0]

  

        for i in range(1, len(nums)):

            num = nums[i]

            current_max = max(num, current_max + num)

            global_max = max(global_max, current_max)

        return global_max
```


Можно решить как я сказал и методом разделяй и властвуй (я об этом тоже думал), но в обоих случаях надо искать пересечения, да и вообще если вдуматься, то было бредовым решением не учитывать то, что эта задача не имеет смысла, если в массиве все числа положительные :) - ну ответом был бы просто max(nums)