---
date: "{{date}}"
tags:
  - problem
level: easy
---
```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-05-12T15:55:22.942Z","endTime":"2025-05-12T16:03:43.374Z"},{"name":"Segment 2","startTime":"2025-05-12T16:03:44.000Z","endTime":"2025-05-12T16:17:44.000Z"}]}
```


# Задача:

Ссылка:
https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=hash-table
Что нужно?
Дана голова связного списка. Нужно определить есть ли цикл в связном списке.

Вход:
head -> ListNode 

**Выводы по constraints:**
узлов в списке может и не быть

Выход:
Boolean

# Теория/рассуждения
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем.


# Code

тривиальное решение:

```python
class Solution(object):

    def hasCycle(self, head):        

        """

        :type head: ListNode

        :rtype: bool

        """

        if not head:

            return False

        passed_nodes = [head]

        nxt = head

        while True:

            nxt = nxt.next

            if nxt is None:

                return False            

            if nxt in passed_nodes:

                return True

            passed_nodes.append(nxt)
```


Решение через slow / fast указатели

```python 
class Solution(object):  

    def hasCycle(self, head):        

        """

        :type head: ListNode

        :rtype: bool

        """

        if not head:

            return False

        fast = slow = head        

        while fast is not None and fast.next is not None:

            slow = slow.next

            fast = fast.next.next

            if slow == fast:

                return True

        return False
```
# Review
Узнал алгоритм зайца и черепахи или по другому **алгоритм Флойда** для поиска цикла