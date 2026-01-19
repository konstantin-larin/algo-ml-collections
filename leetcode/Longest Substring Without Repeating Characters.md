---
date: "{{date}}"
tags:
  - problem
level: medium
---

```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-05-12T18:47:24.276Z","endTime":"2025-05-12T19:23:06.750Z"}]}
```
# Ссылка: 


# Понимание условия

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

Первым пришло в голову просто делать вот так: 
```python
sub_s = ''
max_l = 0
for l in s:
    if l in sub_s:
       max_l = max(max_l, len(sub_s))
       sub_s = l
...........
```
но я понял, что жадный алгоритм здесь не прокатит.
например такая строка 'cabcdefg' при встрече второй c max_l сбросится хотя по факту здесь max_l == 7

пока на ум приходит только решение за O(n^2)

# Код
```python
class Solution(object):

    def lengthOfLongestSubstring(self, s):

        """

        :type s: str

        :rtype: int

        """

        max_length = 0

        n= len(s)

        for i in range(n):                              

            max_l = 1            

            sub = s[i]                        

            for j in range(i + 1, n):

                if s[j] in sub:                    

                    break

                sub += s[j]                

                max_l += 1

            max_length = max(max_length, max_l)

        return max_length	
```
# Ревью
Улучшенный код с использованием двух указателей и хэш таблицы
```python
class Solution(object):

    def lengthOfLongestSubstring(self, s):

        """

        :type s: str

        :rtype: int

        """

        n = len(s)

        char_map = dict()

        left = 0

        max_len = 0

        for right in range(n):

            if s[right] not in char_map or char_map[s[right]] < left:

                char_map[s[right]] = right

                max_len = max(max_len, right - left + 1)

            else:

                left = char_map[s[right]] + 1

                char_map[s[right]] = right            

        return max_len
```

''