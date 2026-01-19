---
date: "{{date}}"
tags:
  - problem
level: easy
---
```simple-time-tracker
{"entries":[{"name":"Segment 1","startTime":"2025-05-12T16:43:26.000Z","endTime":"2025-05-12T16:59:14.000Z"}]}
```


# Задача:

**Ссылка:**
https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=hash-table

**Что нужно?**
найти узел пересечения у двух связных списков

**Вход:**
две головы

**Выводы по constraints:**
может быть такое что одна из голов или они обе None.

**Выход:**

# Теория/рассуждения
- Есть какие-то шаблоны?
- Есть ли возможность декомпозиции на частные случаи или на более простые задачи?
- Достаточно ли знаний алгоритмов и структур данных, чтобы решить эту задачу? Если нет - изучаем.
Самое очевидное конечно же сделать как в тривиальном решении [[Linked List Cycle]] - просто пройтись по обоим спискам до тех пор, пока не найдешь пересекающийся - curr_node in passed_nodes и если не найдешь, то return None. Но я бы хотел решить вот так:
**Follow up:** Could you write a solution that runs in `O(m + n)` time and use only `O(1)` memory?

[[Intersection Of two linked lists 2025-05-12 19.46.45.excalidraw]]
Пришла идея - пройтись по одному списку и пометить все его узлы пройденными. А потом проходиться по второму и уже проверить узлы на то пройдены ли они уже. Но **Note** that the linked lists must **retain their original structure** after the function returns.


Идея: два переключающихся между списками указателя встретиться между друг с другом или будут оба равны None.
# Code
```python
# Definition for singly-linked list.

# class ListNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.next = None

  

class Solution(object):

    def getIntersectionNode(self, headA, headB):

        """

        :type head1, head1: ListNode

        :rtype: ListNode

        """

        pA = headA

        pB = headB

        if pA is None or pB is None:
            return None

  

        while True:

            pA = pA.next

            pB = pB.next            

  

            if pA == pB:

                return pA

  

            if pA is None:

                pA = headB

            if pB is None:

                pB = headA
```
# Review
В общем, идея свапа между списками классная, надо запомнить. 

Более чистая версия:
```python
class Solution(object): def getIntersectionNode(self, headA, headB): 
	if not headA or not headB: 
		return None 
	a, b = headA, headB
	while a != b: 
		a = a.next if a else headB 
		b = b.next if b else headA 		
	return a
```
