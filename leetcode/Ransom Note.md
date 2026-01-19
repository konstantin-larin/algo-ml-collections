---
tags:
  - problem
level: easy
---
Дата: 2025-06-05

# Ссылка: 
https://leetcode.com/problems/ransom-note/submissions/1654687803/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

# Код
```python
from collections import Counter

class Solution(object):

    def canConstruct(self, ransomNote, magazine):

        """

        :type ransomNote: str

        :type magazine: str

        :rtype: bool

        """

        magazine = Counter(magazine)

        for l in ransomNote:

            if l in magazine:

                magazine[l] -= 1

                if magazine[l] < 0:

                    return False

            else:

                return False

        return True
```
# Ревью
Посчитал количество букв у magazine с помощью Counter.
Затем перебором вычитал это количество, а также проверял есть ли там текущая на переборе буква вообще.