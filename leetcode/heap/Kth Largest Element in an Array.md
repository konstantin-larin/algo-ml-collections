---
tags:
  - problem
level: medium
---
Дата: [[15-06-2025]]

# Ссылка: 
https://leetcode.com/problems/kth-largest-element-in-an-array/description/?envType=study-plan-v2&envId=top-interview-150

# Понимание условия
 - Ограничения по времени/памяти
 - Диапазоны входных данных
 - Разбери все случаи, включая крайние, которые будет решать код

# Подход
- Что первым приходит в голову?
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем, если да - можно запускать таймер

#### Что такое Куча (Heap)?

**Куча** — это специальная древовидная структура данных, которая удовлетворяет свойству кучи:

- **Max-Heap (Макс-куча):** В любом узле значение больше или равно значениям его потомков. Максимальный элемент всегда находится в корне.
- **Min-Heap (Мин-куча):** В любом узле значение меньше или равно значениям его потомков. Минимальный элемент всегда находится в корне.

**Приоритетная очередь** — это абстрактный тип данных, который реализуется, как правило, с помощью кучи. Она позволяет эффективно добавлять элементы и извлекать самый высокий или самый низкий приоритет (т.е., минимальный или максимальный элемент).

**Операции кучи:**

- `heapify` (построение кучи из массива): O(N)
- `heappush` (добавление элемента): O(logK)
- `heappop` (извлечение корневого элемента): O(logK)


# Код
```python
import heapq 
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        for num  in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
```
# Ревью
Узнал, что такое куча.

Решение с созданием массива от min до max. Потом считаем количества и вычитаем справа налево количества k раз. Почему то напомнило рюкзак. Алгоритм плох для большого диапазона чисел.
```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)

        count = [0] * (max_value - min_value + 1)

        for num in nums:
            count[num - min_value] += 1
        
        remaining = k
        for i in range(len(count) - 1, -1,-1):
            remaining -= count[i] 

            if remaining <= 0:
                return i + min_value
```

Интересная техника QuickSelect:

```python 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quick_select(left, right):
	        pivot = nums[right]
	        low = left 
	        high = right
		    while low <= high:
				# Двигаем `low` вправо, пока не найдем элемент, который >= pivot 
				# или пока `low` не пересечет `high`
			    while low <= high and nums[low] < pivot:
				    low += 1
				
				# Двигаем `high` влево, пока не найдем элемент, который <= pivot 
				# или пока `high` не пересечет `low`
				while low <= high and nums[high] > pivot:
					high -= 1
					
				# Если `low` и `high` не пересеклись (т.е., `low <= high`), 
				# это значит, что `nums[low]` >= pivot, а `nums[high]` <= pivot. 
				# Они находятся на "неправильных" сторонах от pivot.
				if low <= high:
					nums[low], nums[high] = nums[high], nums[low]
					low += 1
					high -= 1
			if k <= high:
				return quick_select(left, high)
			if k >= low:
				return quick_select(low, right)					
			return nums[k]
		return quick_select(0, len(nums) - 1)
```

![[Kth Largest Element in an Array 2025-06-18 20.56.40.excalidraw]]