---
tags:
  - problem
level: easy
---

Дата: 2025-06-02
```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-06-02T18:07:45.000Z","endTime":"2025-06-02T18:09:23.000Z"}]}
```
# Ссылка: 


# Понимание условия

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
import re

class Solution(object):

    def isPalindrome(self, s):

        """

        :type s: str

        :rtype: bool

        """

        s = ''.join(re.split(r'[^a-zA-Z0-9]+', s)).lower()        

        l = 0

        r = len(s) - 1

        while l < r:

            if s[l] != s[r]:

                return False

            l += 1

            r -= 1

        return True
```
# Ревью
Классика. Два указателя во всей красе.

можно без регулярок почистить:
```python
class Solution: def isPalindrome(self, s: str) -> bool:
s = ''.join(c.lower() for c in s if c.isalnum()) 
```
