---
tags:
  - problem
level: medium
---

Дата: [[18-06-2025]]

# Ссылка: 
https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150


# Понимание условия
- Ограничения по времени/памяти
- Диапазоны входных данных
- Разбери все случаи, включая крайние, которые будет решать код


1 <= n <= 45
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Приходит  идея рекурсии с базовым случаем n == 0
```python
class Solution(object):

    def _step_down(self,  n, steps=[]):

        if n < 0:

            return

        if n == 0:

            self.variants.append(steps)

            return

        self._step_down(n - 1, steps=steps + [1])        

        self._step_down(n - 2, steps=steps + [2])

  

    def climbStairs(self, n):

        """

        :type n: int

        :rtype: int

        """

        self.variants = []

  

        self._step_down(n, [])

        return len(self.variants)       
```

Решение в целом правильное, но на числе 35 уже жестко. 
Очень напоминает Фибоначи. 
Тут надо как-то использовать DP.
Или как будто бы можно перестановками (математика.)

Да! Я понял! DP!

# Код
```python
class Solution(object):    

    def climbStairs(self, n):

        """

        :type n: int

        :rtype: int

        """

        d = [0 for _ in range(n + 1)]

        d[0] = 1

        d[1] = 1        

  

        for i in range(2, n + 1):

            d[i] = d[i - 1] + d[i - 2]        

        return d[n]
```
# Ревью
Освежил DP с кайфом.

Но нашел решение круче по памяти
```python
class Solution: 
	def climbStairs(self, n: int) -> int: 
		if n <= 3: 
			return n 
		prev1 = 3
		prev2 = 2
		cur = 0
		for _ in range(3, n):
			cur = prev1 + prev2
			prev2 = prev1
			prev1 = cur
		return cur
```
