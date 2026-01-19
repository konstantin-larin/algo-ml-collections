---
tags:
  - problem
level: medium
---
Дата: 2025-06-05

# Ссылка: 
https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код
- `1 <= path.length <= 3000`
- `path` consists of English letters, digits, period `'.'`, slash `'/'` or `'_'`.
- `path` is a valid absolute Unix path.
# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер
# Код
```python
class Solution(object):

    def simplifyPath(self, path):

        """

        :type path: str

        :rtype: str

        """        

        path = path.split('/')  

        skip_indices = set()

        n = len(path)

        for i in range(len(path)):

            if path[i] == '..':                

                minus = 1

                while i - minus in skip_indices and minus > 0:

                    minus += 1

                skip_indices.add(i - minus)                  

                skip_indices.add(i)

  

            if path[i] == '' or  path[i] == '.':        

                skip_indices.add(i)    

  
  

        return ('/'+ "/".join([path[i] for i in range(len(path)) if i not in skip_indices]))
```
# Ревью

Сначала думал реализовать регулярными выражениями замену слешей и точек, но потом понял, что куда проще реализовать это перебором и объединить те части пути, которые нужно, слешем.

Нашел решение лучше с помощью стека, но логика примерно такая же, просто у меня 2 * n, а тут все выполняется за n

```python
class Solution: 
	def simplifyPath(self, path: str) -> str: 
	components = path.split("/") 
	st = [] 
	for comp in components: 
		if comp == "" or comp == ".": 
			continue 
		if comp == "..": 
			if st: 
				st.pop() 
		else: 
			st.append(comp) 
	return "/" + "/".join(st)
```
