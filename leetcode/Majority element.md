---
date: "{{date}}"
tags:
  - problem
level: easy
---
```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-05-12T17:30:31.000Z","endTime":"2025-05-12T18:00:34.000Z"}]}
```

# Ссылка: 
https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=hash-table

# Понимание условия

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

посчитать частоты всех уникальных значений в массиве, вывести самую частую.
Сложность по времени O(n), по памяти O(n)
но как решить за линейную сложность без использования памяти?
Идея: отсортировать массив и считать count, пока оно не станет больше n // 2. Сложность по времени O(n logn), по памяти O(1). Но это нелинейная сложность.
# Код

```python
class Solution(object):

    def majorityElement(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        counts = dict()

        majority_count_threshold = len(nums) // 2

        for num in nums:

            if num not in counts:                                            

                counts[num] = 0                

            counts[num] += 1

            if counts[num] > majority_count_threshold:

                return num
```

# Ревью
До чего я не додумался - Алгоритм голосования Мура.
Интуиция, лежащая в основе алгоритма голосования Мура, основана на том факте, что если в массиве есть элемент с большинством голосов, он всегда будет лидировать, даже после столкновения с другими элементами.
```python
class Solution(object):

    def majorityElement(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """        

        count = 0    

        candidate = None

        for num in nums:

            if count == 0:                

                candidate = num

            if num == candidate:

                count += 1

            else:

                count -= 1

        return candidate        
```


Сложность по времени:

Сложность по памяти: 