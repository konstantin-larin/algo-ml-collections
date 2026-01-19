---
tags:
  - problem
level: easy
---

Дата: [[19-06-2025]]

# Ссылка: 
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

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

    def isSubsequence(self, s, t):

        """

        :type s: str

        :type t: str

        :rtype: bool

        """        

        p1 = 0

        p2 = 0

        n_s = len(s)

        n_t = len(t)      

  

        if n_t < n_s:

            return False

  
  

        while p1 < n_s:

            l1 = s[p1]        

  

            while True:

                if p2 == n_t:                    

                    return False

                l2 = t[p2]

                p2 += 1

                if l1 == l2:                    

                    break

            p1 += 1                    

  

        return True
```
# Ревью

Та же идея с двумя указателями, но лучшая реализация:


```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)
```

