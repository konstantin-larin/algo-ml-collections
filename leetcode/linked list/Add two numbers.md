---
tags:
  - problem
level: medium
---

Дата: 2025-06-05

# Ссылка: 
https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150


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
# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution(object):

    def addTwoNumbers(self, l1, l2):

        """

        :type l1: Optional[ListNode]

        :type l2: Optional[ListNode]

        :rtype: Optional[ListNode]

        """        

        d = 0

        head1 = l1

        head2 = l2        

        head3 = ListNode()

        nxt = head3

  

        while True:

            val = d

            if head1 is not None:                

                val += head1.val

                head1 = head1.next          

            if head2 is not None:

                val += head2.val

                head2 = head2.next

            if val > 9:

                val -= 10

                d = 1    

            else:

                d = 0

  

            nxt.val = val                    

  

            if head1 is None and head2 is None:

                if d == 1:

                    nxt.next = ListNode(d)              

                return head3

            nxt.next = ListNode()

            nxt = nxt.next
```
# Ревью
Уже был знаком со связным списком, ничего сложного в задаче не увидел.
