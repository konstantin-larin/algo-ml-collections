---
tags:
  - problem
level: medium
---

Дата: [[15-06-2025]]

# Ссылка: 
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Первым приходит в голову просто хэш таблицу создать из цифр и прилежащих к ним букв и проходом пушить комбинации.
# Код
```python
from collections import deque

class Solution(object):

    def letterCombinations(self, digits):

        """

        :type digits: str

        :rtype: List[str]

        """

        d_map = {

            '2': 'abc',

            '3': 'def',

            '4': 'ghi',

            '5': 'jkl',

            '6': 'mno',

            '7': 'pqrs',

            '8': 'tuv',

            '9': 'wxyz',

        }

        n = len(digits)

        if n == 0:

            return []        

        queue = deque(d_map[digits[0]])

        for i in range(1, n):

            d = digits[i]

            letters = d_map[d]            

            # в конец очереди вставляем новые комбинации

            # из начала берем старые комбинации

            # заканчиваем цикл, когда старых комбинаций не осталось

            # то есть когда len(queue[0]) > i

            while True:

                if len(queue[0]) > i:

                    break

                old = queue.popleft()

                for l in letters:

                    queue.append(old + l)

        return list(queue)
```
# Ревью
Использовал преимущества структуры deque
Иное решение рекурсией:
```python
class Solution:

    def letterCombinations(self, digits):

        if not digits:

            return []

        digit_to_letters = {

            '2': 'abc',

            '3': 'def',

            '4': 'ghi',

            '5': 'jkl',

            '6': 'mno',

            '7': 'pqrs',

            '8': 'tuv',

            '9': 'wxyz',

        }

  

        def backtrack(idx, comb):

            if idx == len(digits):

                res.append(comb)

                return

            for letter in digit_to_letters[digits[idx]]:

                backtrack(idx + 1, comb + letter)

  

        res = []

        backtrack(0, "")

  

        return res
```