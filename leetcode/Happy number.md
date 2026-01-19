---
date: "{{date}}"
tags:
  - problem
level: easy
---

```simple-time-tracker
```
# Ссылка: 
https://leetcode.com/problems/happy-number/description/?envType=problem-list-v2&envId=hash-table

# Понимание условия

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
class Solution(object):

    def isHappy(self, n):

        """

        :type n: int

        :rtype: bool

        """

        passed_values = set()        

        while True:

            new_n = 0            

            for d in str(n):

                new_n += int(d) ** 2

            if new_n == 1:

                return True

            if new_n in passed_values:

                return False

            passed_values.add(new_n)

            n = new_n
```
# Ревью

Сложность по времени:

Сложность по памяти: 